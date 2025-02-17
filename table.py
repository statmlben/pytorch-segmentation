import pandas as pd

## VOC dataset
d1 = {'method': 'T', 'metric': 'IoU', 'loss': 'CE', 0: 0.862, 1: 0.634, 2: 0.259, 3: 0.682, 4: 0.427, 5: 0.358, 6: 0.683, 7: 0.475, 8: 0.692, 9: 0.128, 10: 0.586, 11: 0.275, 12: 0.579, 13: 0.553, 14: 0.606, 15: 0.577, 16: 0.202, 17: 0.474, 18: 0.25, 19: 0.71, 20: 0.414}
d2 = {'method': 'T', 'metric': 'Dice', 'loss': 'CE', 0: 0.914, 1: 0.712, 2: 0.371, 3: 0.76, 4: 0.511, 5: 0.428, 6: 0.728, 7: 0.535, 8: 0.75, 9: 0.175, 10: 0.653, 11: 0.329, 12: 0.646, 13: 0.639, 14: 0.697, 15: 0.67, 16: 0.269, 17: 0.539, 18: 0.298, 19: 0.777, 20: 0.484}
d3 = {'method': 'rankdice', 'metric': 'IoU', 'loss': 'CE', 0: 0.863, 1: 0.634, 2: 0.273, 3: 0.687, 4: 0.429, 5: 0.368, 6: 0.696, 7: 0.49, 8: 0.697, 9: 0.144, 10: 0.599, 11: 0.292, 12: 0.587, 13: 0.566, 14: 0.626, 15: 0.581, 16: 0.22, 17: 0.479, 18: 0.269, 19: 0.711, 20: 0.42}
d4 = {'method': 'rankdice', 'metric': 'Dice', 'loss': 'CE', 0: 0.914, 1: 0.713, 2: 0.387, 3: 0.766, 4: 0.513, 5: 0.442, 6: 0.741, 7: 0.55, 8: 0.755, 9: 0.196, 10: 0.665, 11: 0.345, 12: 0.655, 13: 0.653, 14: 0.716, 15: 0.674, 16: 0.291, 17: 0.543, 18: 0.32, 19: 0.779, 20: 0.492}

d5 = {'method': 'T', 'metric': 'IoU', 'loss': 'focal', 0: 0.848, 1: 0.592, 2: 0.124, 3: 0.652, 4: 0.491, 5: 0.3, 6: 0.675, 7: 0.456, 8: 0.679, 9: 0.116, 10: 0.537, 11: 0.274, 12: 0.634, 13: 0.583, 14: 0.567, 15: 0.554, 16: 0.173, 17: 0.554, 18: 0.244, 19: 0.689, 20: 0.416}
d6 = {'method': 'T', 'metric': 'Dice', 'loss': 'focal', 0: 0.905, 1: 0.684, 2: 0.196, 3: 0.743, 4: 0.595, 5: 0.362, 6: 0.723, 7: 0.511, 8: 0.741, 9: 0.167, 10: 0.601, 11: 0.336, 12: 0.71, 13: 0.673, 14: 0.655, 15: 0.65, 16: 0.224, 17: 0.628, 18: 0.298, 19: 0.758, 20: 0.507}
d7 = {'method': 'rankdice', 'metric': 'IoU', 'loss': 'focal', 0: 0.844, 1: 0.641, 2: 0.206, 3: 0.664, 4: 0.515, 5: 0.314, 6: 0.688, 7: 0.479, 8: 0.687, 9: 0.161, 10: 0.56, 11: 0.324, 12: 0.649, 13: 0.601, 14: 0.579, 15: 0.576, 16: 0.207, 17: 0.586, 18: 0.29, 19: 0.704, 20: 0.454}
d8 = {'method': 'rankdice', 'metric': 'Dice', 'loss': 'focal', 0: 0.902, 1: 0.727, 2: 0.305, 3: 0.758, 4: 0.619, 5: 0.376, 6: 0.735, 7: 0.536, 8: 0.754, 9: 0.222, 10: 0.623, 11: 0.386, 12: 0.725, 13: 0.695, 14: 0.67, 15: 0.672, 16: 0.269, 17: 0.66, 18: 0.346, 19: 0.773, 20: 0.541}

d9 = {'method': 'T', 'metric': 'IoU', 'loss': 'BCE', 0: 0.455, 1: 0.365, 2: 0.073, 3: 0.371, 4: 0.278, 5: 0.196, 6: 0.374, 7: 0.244, 8: 0.366, 9: 0.051, 10: 0.324, 11: 0.159, 12: 0.359, 13: 0.335, 14: 0.335, 15: 0.337, 16: 0.128, 17: 0.311, 18: 0.168, 19: 0.401, 20: 0.268}
d10 = {'method': 'T', 'metric': 'Dice', 'loss': 'BCE', 0: 0.909, 1: 0.729, 2: 0.146, 3: 0.742, 4: 0.555, 5: 0.391, 6: 0.748, 7: 0.489, 8: 0.731, 9: 0.102, 10: 0.649, 11: 0.317, 12: 0.717, 13: 0.67, 14: 0.669, 15: 0.674, 16: 0.255, 17: 0.621, 18: 0.337, 19: 0.803, 20: 0.537}
d11 = {'method': 'rankdice', 'metric': 'IoU',  'loss': 'BCE',0: 0.457, 1: 0.376, 2: 0.115, 3: 0.381, 4: 0.305, 5: 0.206, 6: 0.379, 7: 0.259, 8: 0.376, 9: 0.073, 10: 0.342, 11: 0.176, 12: 0.372, 13: 0.354, 14: 0.351, 15: 0.348, 16: 0.143, 17: 0.334, 18: 0.194, 19: 0.411, 20: 0.282}
d12 = {'method': 'rankdice',  'metric': 'Dice', 'loss': 'BCE',0: 0.914, 1: 0.753, 2: 0.231, 3: 0.763, 4: 0.61, 5: 0.411, 6: 0.759, 7: 0.517, 8: 0.751, 9: 0.145, 10: 0.684, 11: 0.353, 12: 0.744, 13: 0.709, 14: 0.701, 15: 0.697, 16: 0.286, 17: 0.669, 18: 0.389, 19: 0.821, 20: 0.564}

list_of_dicts = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]

d = {}
for k in d1.keys():
  d[k] = tuple(d[k] for d in list_of_dicts)

df = pd.DataFrame(d)
df[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]] = df[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]*100

## CityScapes dataset

d1 = {'method': 'T', 'metric': 'IoU', 'loss': 'CE', 0: 0.772, 1: 0.478, 2: 0.762, 3: 0.136, 4: 0.109, 5: 0.29, 6: 0.265, 7: 0.39, 8: 0.841, 9: 0.201, 10: 0.77, 11: 0.363, 12: 0.273, 13: 0.769, 14: 0.219, 15: 0.422, 16: 0.307, 17: 0.158, 18: 0.325}
d2 = {'method': 'T', 'metric': 'Dice', 'loss': 'CE', 0: 0.857, 1: 0.573, 2: 0.846, 3: 0.174, 4: 0.147, 5: 0.419, 6: 0.349, 7: 0.499, 8: 0.902, 9: 0.257, 10: 0.836, 11: 0.451, 12: 0.351, 13: 0.841, 14: 0.247, 15: 0.468, 16: 0.349, 17: 0.197, 18: 0.414}
d3 = {'method': 'rankdice', 'metric': 'IoU', 'loss': 'CE', 0: 0.771, 1: 0.508, 2: 0.767, 3: 0.164, 4: 0.117, 5: 0.317, 6: 0.283, 7: 0.401, 8: 0.841, 9: 0.231, 10: 0.778, 11: 0.4, 12: 0.292, 13: 0.766, 14: 0.233, 15: 0.465, 16: 0.315, 17: 0.177, 18: 0.326}
d4 = {'method': 'rankdice', 'metric': 'Dice', 'loss': 'CE', 0: 0.856, 1: 0.608, 2: 0.851, 3: 0.21, 4: 0.158, 5: 0.46, 6: 0.374, 7: 0.514, 8: 0.903, 9: 0.294, 10: 0.845, 11: 0.495, 12: 0.372, 13: 0.84, 14: 0.266, 15: 0.513, 16: 0.358, 17: 0.222, 18: 0.419}

d5 = {'method': 'T', 'metric': 'IoU', 'loss': 'BCE', 0: 0.461, 1: 0.219, 2: 0.397, 3: 0.024, 4: 0.076, 5: 0.135, 6: 0.094, 7: 0.176, 8: 0.445, 9: 0.099, 10: 0.4, 11: 0.164, 12: 0.093, 13: 0.404, 14: 0.109, 15: 0.182, 16: 0.169, 17: 0.035, 18: 0.165}
d6 = {'method': 'T', 'metric': 'Dice', 'loss': 'BCE', 0: 0.922, 1: 0.438, 2: 0.794, 3: 0.049, 4: 0.152, 5: 0.271, 6: 0.187, 7: 0.353, 8: 0.89, 9: 0.198, 10: 0.801, 11: 0.328, 12: 0.186, 13: 0.808, 14: 0.218, 15: 0.363, 16: 0.338, 17: 0.07, 18: 0.329}
d7 = {'method': 'rankdice', 'metric': 'IoU', 'loss': 'BCE', 0: 0.461, 1: 0.27, 2: 0.41, 3: 0.042, 4: 0.095, 5: 0.182, 6: 0.106, 7: 0.198, 8: 0.447, 9: 0.127, 10: 0.403, 11: 0.193, 12: 0.12, 13: 0.406, 14: 0.134, 15: 0.196, 16: 0.174, 17: 0.044, 18: 0.184}
d8 = {'method': 'rankdice', 'metric': 'Dice', 'loss': 'BCE', 0: 0.922, 1: 0.54, 2: 0.821, 3: 0.083, 4: 0.191, 5: 0.364, 6: 0.213, 7: 0.396, 8: 0.894, 9: 0.253, 10: 0.807, 11: 0.386, 12: 0.24, 13: 0.812, 14: 0.268, 15: 0.392, 16: 0.347, 17: 0.087, 18: 0.367}

d9 = {'method': 'T', 'metric': 'IoU', 'loss': 'Focal', 0: 0.779, 1: 0.438, 2: 0.748, 3: 0.124, 4: 0.089, 5: 0.234, 6: 0.24, 7: 0.351, 8: 0.838, 9: 0.185, 10: 0.752, 11: 0.341, 12: 0.24, 13: 0.762, 14: 0.227, 15: 0.438, 16: 0.31, 17: 0.161, 18: 0.329}
d10 = {'method': 'T', 'metric': 'Dice', 'loss': 'Focal', 0: 0.861, 1: 0.536, 2: 0.834, 3: 0.161, 4: 0.124, 5: 0.347, 6: 0.315, 7: 0.459, 8: 0.902, 9: 0.241, 10: 0.82, 11: 0.426, 12: 0.312, 13: 0.834, 14: 0.256, 15: 0.488, 16: 0.363, 17: 0.204, 18: 0.421}
d11 = {'method': 'rankdice', 'metric': 'IoU', 'loss': 'Focal', 0: 0.777, 1: 0.484, 2: 0.747, 3: 0.168, 4: 0.098, 5: 0.231, 6: 0.247, 7: 0.351, 8: 0.828, 9: 0.227, 10: 0.762, 11: 0.382, 12: 0.263, 13: 0.74, 14: 0.248, 15: 0.468, 16: 0.322, 17: 0.168, 18: 0.325}
d12 = {'method': 'rankdice', 'metric': 'Dice', 'loss': 'Focal', 0: 0.86, 1: 0.587, 2: 0.836, 3: 0.215, 4: 0.137, 5: 0.356, 6: 0.335, 7: 0.466, 8: 0.896, 9: 0.287, 10: 0.831, 11: 0.476, 12: 0.339, 13: 0.818, 14: 0.281, 15: 0.515, 16: 0.373, 17: 0.211, 18: 0.42}

list_of_dicts = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]

d = {}
for k in d1.keys():
  d[k] = tuple(d[k] for d in list_of_dicts)

df = pd.DataFrame(d)