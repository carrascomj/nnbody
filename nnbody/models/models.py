"""Custom layers for graph convolutional neural networks."""
import torch.nn as nn
import torch.nn.functional as F

from .layers import GraphConvolution, NormalizationLayer


class GCN_simple(nn.Module):
    """Simplest GCN model."""

    def __init__(
        self,
        feats,
        hidden,
        label,
        nb_nodes,
        dropout,
        bias=False,
        act=F.relu,
        cuda=False,
    ):
        """Initialize GCN model.

        Parameters
        ----------
        feats: int
            dimension of inputs
        hidden: Iterable[int]
            a vector of dimensions of the hidden graph convolutional layers
        label: int
            dimension of output
        nb_nodes: int
            number of aminoacids. Used for last layer.
        dropout: float
        bias: bool (False)
        act: function
            activation function. Default: F.relu
        cuda: bool
            important to correctly sparsize

        """
        super(GCN_simple, self).__init__()
        hidden = [hidden] if isinstance("hidden", int) else hidden
        gc_layers = [
            GraphConvolution(in_dim, out_dim, dropout, bias, act)
            for in_dim, out_dim in zip([feats] + hidden[:-1], hidden)
        ]
        self.hidden_layers = nn.Sequential(*gc_layers)
        self.out_layer = nn.Linear(nb_nodes, label)
        # self.out_layer = nn.Sequential(
        #     nn.Flatten(), nn.Linear(nb_nodes * hidden[-1], label)
        # )
        self.in_cuda = cuda

    def forward(self, input):
        """Pass forward GCN model.

        Parameters
        ----------
        input:
            v: torch.Tensor
                3D Tensor containing the features of nodes
            adj: torch.Tensor
                3D tensor with the values of the adjacency matrix

        """
        v, adj = input
        input = [v, adj]
        x, _ = self.hidden_layers.forward(input)
        x = x.sum(axis=-1)
        x = self.out_layer(x)
        return x


class GCN_normed(nn.Module):
    """Simplest GCN model."""

    def __init__(
        self,
        feats,
        hidden,
        label,
        nb_nodes,
        dropout,
        bias=False,
        act=F.relu,
        D=1,
        cuda=False,
    ):
        """Initialize GCN model.

        Parameters
        ----------
        feats: int
            dimension of inputs
        hidden: Iterable[int]
            a vector of dimensions of the hidden graph convolutional layers
        label: int
            dimension of output
        nb_nodes: int
            number of aminoacids. Used for last layer.
        dropout: float
        bias: bool (False)
        act: function
            activation function. Default: F.relu
        D: int
            initial diameter for normalization
        cuda: bool
            important to correctly sparsize

        """
        super(GCN_normed, self).__init__()
        self.in_cuda = cuda
        hidden = [hidden] if isinstance("hidden", int) else hidden
        gc_layers = [
            nn.Sequential(
                NormalizationLayer(in_dim, D=D),
                GraphConvolution(in_dim, out_dim, dropout, bias, act),
            )
            for in_dim, out_dim in zip([feats] + hidden[:-1], hidden)
        ]
        self.hidden_layers = nn.Sequential(*gc_layers)
        self.out_layer = nn.Sequential(
            nn.Flatten(), nn.Linear(nb_nodes * hidden[-1], label)
        )

    def forward(self, input):
        """Pass forward GCN model.

        Parameters
        ----------
        input:
            v: torch.Tensor
                3D Tensor containing the features of nodes
            adj: torch.Tensor
                3D tensor with the values of the adjacency matrix

        """
        v, adj = input
        x, _ = self.hidden_layers.forward(input)
        x = self.out_layer(x)
        return x


class FFNN(nn.Module):
    """Plain Feed Forward Neural Network."""

    def __init__(
        self, feats, hidden, label, nb_nodes, dropout, cuda=False,
    ):
        """Initialize FFNN model.

        The activation function is set to Relu.

        Parameters
        ----------
        feats: int
            dimension of inputs
        hidden: Iterable[int]
            a vector of dimensions of the hidden graph convolutional layers
        label: int
            dimension of output
        nb_nodes: int
            number of aminoacids. Used for last layer.
        dropout: float
        cuda: bool
            important to correctly sparsize

        """
        super(FFNN, self).__init__()
        hidden = [hidden] if isinstance("hidden", int) else hidden
        gc_layers = [
            nn.Sequential(
                nn.Linear(in_dim, out_dim), nn.ReLU(), nn.Dropout(dropout)
            )
            for in_dim, out_dim in zip([feats] + hidden[:-1], hidden)
        ]
        self.hidden_layers = nn.Sequential(*gc_layers)
        self.out_layer = nn.Sequential(
            nn.Flatten(), nn.Linear(nb_nodes * hidden[-1], label)
        )
        self.in_cuda = cuda

    def forward(self, input):
        """Pass forward GCN model.

        Parameters
        ----------
        input:
            v: torch.Tensor
                3D Tensor containing the features of nodes
            adj: torch.Tensor
                3D tensor with the values of the adjacency matrix

        """
        v, adj = input
        x = self.hidden_layers.forward(v)
        x = self.out_layer(x)
        return x
