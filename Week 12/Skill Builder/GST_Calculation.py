#GST Calculation
#Create a parent class 'Event' with the following attributes.
#Parent class: Event event_type, event_name, event_detail, owner_name, cost_per_day, start_date, end_date (event_type is Exhibition / StageEvent)
#Create child classes Exhibition and StageEvent for the parent class Event.
#Child class: Exhibition    Method: to calculate total cost and GST
#Child class: StageEvent    Method: to calculate total cost and GST


from datetime import date

class Event:
    def __init__(self, event_type, event_name, event_details, owner_name, cost_per_day, start_date, end_date):
        self.event_type = event_type
        self.event_name = event_name
        self.event_details =  event_details
        self.owner_name = owner_name
        self.cost_per_day = cost_per_day
        self.start_date = start_date
        self.end_date =  end_date


class Exhibition(Event):
    
    def calculate_GST(self):
        
        
        s_date_list = self.start_date.split('-')
        s_date_y = int(s_date_list[0])
        s_date_m = int(s_date_list[1])
        s_date_d = int(s_date_list[2])

        e_date_list = self.end_date.split('-')
        e_date_y = int(e_date_list[0])
        e_date_m = int(e_date_list[1])
        e_date_d = int(e_date_list[2])
        
        d1 = date(e_date_y, e_date_m, e_date_d)
        d2 = date(s_date_y, s_date_m, s_date_d)

        date_diff = d1 - d2
      

        total_cost = self.cost_per_day * date_diff.days
        print(total_cost)
        gst_value = 0.05 * total_cost
        print(gst_value)

class StageEvent(Event):
    
    def calculate_GST(self):
        
        
        s_date_list = self.start_date.split('-')
        s_date_y = int(s_date_list[0])
        s_date_m = int(s_date_list[1])
        s_date_d = int(s_date_list[2])

        e_date_list = self.end_date.split('-')
        e_date_y = int(e_date_list[0])
        e_date_m = int(e_date_list[1])
        e_date_d = int(e_date_list[2])
        
        d1 = date(e_date_y, e_date_m, e_date_d)
        d2 = date(s_date_y, s_date_m, s_date_d)

        date_diff = d1 - d2
        

        total_cost = self.cost_per_day * date_diff.days
        print(total_cost)
        gst_value = 0.15 * total_cost
        print(gst_value)



event_type = input()
event_name = input()
event_details = input()
owner_name = input()
cost_per_day = float(input())
start_date = input()
end_date = input()

if event_type == 'Exhibition':
    obj = Exhibition(event_type, event_name, event_details, owner_name, cost_per_day, start_date, end_date)
    obj.calculate_GST()

elif event_type == 'StageEvent':
    obj = StageEvent(event_type, event_name, event_details, owner_name, cost_per_day, start_date, end_date)
    obj.calculate_GST()