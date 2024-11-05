from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import QPointF
import pickle

# Convert QPolygonF to list of tuples
polygon = QPolygonF([QPointF(0, 0), QPointF(1, 1), QPointF(2, 0)])
points = [(point.x(), point.y()) for point in polygon]

# Serialize the list
with open('polygon.pkl', 'wb') as f:
    pickle.dump(points, f)

# Deserialize the list
with open('polygon.pkl', 'rb') as f:
    loaded_points = pickle.load(f)

# Convert back to QPolygonF
reconstructed_polygon = QPolygonF([QPointF(x, y) for x, y in loaded_points])
print(reconstructed_polygon.data)