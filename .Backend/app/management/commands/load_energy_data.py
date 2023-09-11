from django.core.management.base import BaseCommand
from app.models import EnergyData
import json
from datetime import datetime

class Command(BaseCommand):
    help = 'Load energy data from JSON file into the database'

    def handle(self, *args, **options):
        json_file_path = '/home/faizan/Assignment/dashboard/app/management/commands/Data.json'



        with open(json_file_path, 'r') as file:
            data = json.load(file)
            print(len(data))

            for item in data:
                # Check if 'intensity' key exists and provide a default value if not
                intensity = item.get('intensity', 0)  # You can adjust the default value as needed

                # Check if 'pestle' key exists and provide a default value if not
                pestle = item.get('pestle', 'DefaultPestleValue')

                source = item.get('source' ,  "Null")
                 
                title = item.get('title' , 'null')  
                likelihood = item.get('likelihood', 0) 
    
           
                added_input_datetime = item['added']
                input_datetime1 = datetime.strptime(added_input_datetime , "%B, %d %Y %H:%M:%S")
                added_formatted_datetime= input_datetime1.strftime("%Y-%m-%d %H:%M:%S")
                
                
                if item['published'] == '':
                    item['published'] == "0-0-0 0:0:0"
            
                
                else :
                      published_input_datetime = item['published']
                      input_datetime2 = datetime.strptime(published_input_datetime  , "%B, %d %Y %H:%M:%S")
                      published_formatted_datetime = input_datetime2.strftime("%Y-%m-%d %H:%M:%S")
             

                EnergyData.objects.create(
                    end_year=item['end_year'],
                    intensity=intensity,  # Use the 'intensity' variable with default value
                    sector=item['sector'],
                    topic=item['topic'],
                    insight=item['insight'],
                    url=item['url'],
                    region=item['region'],
                    start_year=item['start_year'],
                    impact=item['impact'],
                    source = source,
                    title = title,
                    added =  added_formatted_datetime,
                    published = published_formatted_datetime,
                  
                    country=item['country'],
                    relevance=item['relevance'],
                    pestle=pestle, 
                    # added = added_datetime ,
                    # published =  published_datetime # Use the 'pestle' variable with default value
                    likelihood= likelihood    
                )
     
              

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from JSON file.'))
       