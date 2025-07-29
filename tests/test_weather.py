import unittest
import vcr
from weather.weather import get_city_coordinates, get_weather


my_vcr = vcr.VCR(
    cassette_library_dir='tests/fixtures/cassettes',
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
)

class WeatherTests(unittest.TestCase):

    @my_vcr.use_cassette('test_get_city_coordinates')
    def test_get_city_coordinates_valid_city(self):
        data = get_city_coordinates("London")
        self.assertIn('latitude', data)
        self.assertIn('longitude', data)

    @my_vcr.use_cassette('test_get_weather_valid_city')
    def test_get_weather_valid_city(self):
        result = get_weather("New York")
        self.assertIn('temperature', result)
        self.assertIn('rain', result)
        self.assertIn('relative_humidity', result)
        self.assertEqual(result['city'], "New York")

    @my_vcr.use_cassette('test_get_city_coordinates_invalid_city')
    def test_get_city_coordinates_invalid_city(self):
        with self.assertRaises(Exception):
            get_city_coordinates("ThisCityDoesNotExist123")

    @my_vcr.use_cassette('test_get_weather_invalid_city')
    def test_get_weather_invalid_city(self):
        result = get_weather("InvalidCityName")
        self.assertIn("not found", result)

