# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator

rect = shape_calculator.Rectangle(10, 3)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
