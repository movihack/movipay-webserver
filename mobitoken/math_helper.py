class MathHelper(object):
	"""docstring for MathHelper"""
	@staticmethod
	def heversine(lat_a, lng_a, lat_b, lng_b):
		lat_a = (lat_a * math.pi) / 180.0
		lng_a = (lng_a * math.pi) / 180.0
		lat_b = (lat_b * math.pi) / 180.0
		lng_b = (lng_b * math.pi) / 180.0

		delta_lat = lat_a - lat_b
		delta_lng = lng_a - lng_b

		a = math.sin(delta_lat / 2.0) * math.sin(delta_lat / 2.0) +
			math.cos(lat_b) * math.cos(lat_a) *
			math.sin(delta_lng / 2.0) * math.sin(delta_lng / 2.0)

		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

		return (6371  * 1000) * c