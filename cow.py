class Cow:
     # Initialize a new Cow object with a name and sets the image to None
    def __init__(self, name):
        self.name = name
        self.image = None

    def get_name(self):
        # Return the name of the Cow object
        return self.name

    def get_image(self):
        # Return the image of the Cow object
        return self.image

    def set_image(self, image):
        # Set the image of the Cow object to the given image parameter
        self.image = image
