import random
from PyQt5 import QtWidgets, QtGui


class MealGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create the UI elements
        self.label = QtWidgets.QLabel("Enter your current weight:")
        self.weight_input = QtWidgets.QLineEdit()
        self.generate_button = QtWidgets.QPushButton("Generate Meal")
        self.meal_label = QtWidgets.QLabel("")

        # Create a layout to organize the UI elements
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.meal_label)
        self.setLayout(layout)

        # Connect the generate button to the generate_meal function
        self.generate_button.clicked.connect(self.generate_meal)

        # Set the window title and size
        self.setWindowTitle("Meal Generator")
        self.setGeometry(400, 400, 300, 150)

    def generate_meal(self):
        # Read the current weight from the weight input field
        weight = self.weight_input.text()

        # Generate a random meal from a list of options
        meals = ["grilled chicken with vegetables", "quinoa and black bean salad", "baked salmon with sweet potato",
                 "vegetable stir-fry with tofu"]
        meal = random.choice(meals)

        # Update the meal label with the generated meal
        self.meal_label.setText(meal)

        # Save the current weight to a database or file
        # (Implementation details will depend on your specific needs and preferences)
        with open("weight_data.txt", "w") as f:
            f.write(weight)


# Run the application
app = QtWidgets.QApplication([])
window = MealGenerator()
window.show()
app.exec_()
