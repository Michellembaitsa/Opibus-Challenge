class DriverControl:
      def __init__(self):
          pass
      def drive(self):
            pass
class DriverControlAdvanced(DriverControl): #Thenew class inherits the DriverControl class.
      def __init__(self):
          super().__init__() #super acts to override the previous class.
      def eco(self):
            pass
      def sport(self):
            pass
      def offRoad(self):
            pass