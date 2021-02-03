class MyData:

	def __init__(self):
		self.data = [
			[
				{"content": "this is content1"},
				{"content": "this is content2"},
				{"content": "this is content3"},
				{"content": "this is content4"},
			],
			[
				{"content": "this is content6"},
			]
		]
	
	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data 