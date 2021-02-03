class MyData:

	def __init__(self):
		self.data = [
			[
				"content1",
				"content2",
				"content3",
			],
			[
				"content1",
				"content2",
			]
		]
	
	def get_data(self):
		return self.data

	def set_data(self, dta):
		self.data = dta