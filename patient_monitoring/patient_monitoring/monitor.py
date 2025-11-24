import numpy as np

class PatientMonitor:
    def __init__(self):
        self.history = []

    def preprocess(self, hr, spo2, temp):
        arr = np.array([hr, spo2, temp], dtype=float)
        self.history.append(arr)
        return arr

    def analyze(self, arr):
        hr, spo2, temp = arr

        status = []
        if hr < 60 or hr > 100:
            status.append("Abnormal Heart Rate")

        if spo2 < 95:
            status.append("Low SpO2")

        if temp < 36 or temp > 37.5:
            status.append("Abnormal Temperature")

        if not status:
            return "Stable"
        return ", ".join(status)
