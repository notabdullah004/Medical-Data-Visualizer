import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_draw_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)
        self.assertEqual(fig.__class__.__name__, 'Figure')

    def test_draw_heat_map(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)
        self.assertEqual(fig.__class__.__name__, 'Figure')

if __name__ == '__main__':
    unittest.main()
