class AdmissionStatus:

    PENDING = 0
    APPROVED = 1
    AFFIRMATIVE = 2
    DENIED = 3

    @staticmethod
    def get_choices():
        return (
            (AdmissionStatus.PENDING, 'Pending'),
            (AdmissionStatus.APPROVED, 'Approved'),
            (AdmissionStatus.AFFIRMATIVE, 'Affirmative'),
            (AdmissionStatus.DENIED, 'Denied'),
        )