from django.db import models
from employee.models import Employee

# Create your models here.
class WorkShifts(models.Model):
    shifts = [("Morning","morning shift"),
              (:"Night","NightShift"),
              ]
    name = models.CharField(max_length=100,unique=True)
    shift_type = models.CharField(max_length=20,choices=shifts)
    start_time = models.DateField()
    end_time = models.DateField()
    
    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
        
    
class attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.ForeignKey(WorkShifts,on_delete= models.SET_NULL,unique=True,blank=True)
    clock_in = models.TimeField()
    clock_out = models.TimeField()
    is_present = models.BooleanField(default =True)
    
    def total_hours_worked(self):
        if self.clock_in and self.clock_out:
            return(datetime.combine(date.today() - self.clock_out)-
                   datetime.combine(date.today() - self.clock_in)).seconds/3600
        return 0
    
    def __str__(self):
        return f"{self.employee} - {self.date} - {'Present' if self.is_present else 'Absent'}"    
    