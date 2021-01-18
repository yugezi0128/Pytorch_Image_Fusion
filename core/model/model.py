import torch
import torch.nn as nn


class dense(nn.Module):
	"""docstring for dense"""

	def __init__(self, in_channels, out_channels, num_layers):
		super(dense, self).__init__()
		self.dense_block = nn.ModuleList([nn.Sequential(
			nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, padding=1),
			nn.BatchNorm2d(out_channels),
			nn.ReLU()) if i == 0 else nn.Sequential(
			nn.Conv2d(in_channels=out_channels * i, out_channels=out_channels, kernel_size=3, padding=1),
			nn.BatchNorm2d(out_channels),
			nn.ReLU()) for i in range(num_layers)])

	def forward(self, inputs):
		feats = [inputs]
		for block in self.dense_block:
			feat = block(torch.cat(feats, dim=1)) if len(feats)==1 else block(torch.cat(feats[1:], dim=1))
			feats.append(feat)
		return torch.cat(feats[1:], dim=1)
