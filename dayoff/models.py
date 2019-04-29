from django.db import models

# Create your models here.
class DayOff(models.Model):
    create_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    reason = models.TextField()
    PERSONAL = 'ลากิจ'
    SICK = 'ลาป่วย'
    TYPES = (
        (PERSONAL, 'ลากิจ'),
        (SICK, 'ลาป่วย')
    )
    type = models.CharField(max_length=6, choices=TYPES, default='ลากิจ')

    date_start = models.DateField()
    date_end = models.DateField()

    WAIT = 'รอการอนุมัติ'
    APPROVE = 'อนุมัติ'
    NAPPROVE = 'ไม่อนุมัติ'
    TYPES2 = (
        (WAIT, 'รอการอนุมัติ'),
        (APPROVE, 'อนุมัติ'),
        (NAPPROVE, 'ไม่อนุมัติ')
    )
    approve_status = models.CharField(max_length=12, choices=TYPES2, default='รอการอนุมัติ')

    def __str__(self):
        return self.approve_status
