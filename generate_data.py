

import os
import logging
import django
from datetime import datetime
import random
# configure logging settings
logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)

# configure Django settings for import
script_dir = os.path.dirname(__file__)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


# load django models, do not move up, needs te be after django has been setup
from plants.models import Energie_import, Energie_export, Project, Project_kerngetallen, Vestiging, Bedrijf

def generate_bedrijven():
    """Generate random companies"""

    logger.info("Started loading data for model Bedrijf at: " +
                datetime.now().strftime("%H:%M:%S"))

    companynames = [
        'Moen',
        'Jast',
        'Abbott-Borer',
        'Flatley Group',
        'Towne',
        'Conn',
        'Skiles',
        'Stokes',
        'Champlin',
        'Hills',
        'Volkman',
        'Kunze',
        'Koch',
        'Lowe',
        'Wiza Ltd'

    ]

    sectornames = {
        '1': 'Aardolie en aardgaswinning',
        '2': 'Berg- en steengroeven',
        '3': 'Papier- en kartonproductie',
        '4': 'Chemische productie',
        '5': 'Voedingsmiddelenproductie',
        '6': 'Pharmaceutische productie',
    }

    belangerenigingen = {
        '1': 'Energie en oliebedrijven',
        '2': 'Winningsbedrijven Nederland',
        '3': 'Nederlandse Vereniging van Papier- en Kartonfabrikanten',
        '4': 'Cluster Chemie',
        '5': 'Nederlandse Vereniging van Voedingsmiddelenindustrie',
        '6': 'Pharma Nederland',
        }

    for company in companynames:
        print(company)
        try:
            bedrijf = Bedrijf(
                naam = company,
                sector = sectornames[str(random.randint(1, 6))],
                belangenvereniging = belangerenigingen[str(random.randint(1, 5))],
            )
            bedrijf.save()

            logger.debug('Succesfully saved ' + str(company))
        except Exception as e:
            logger.error('Could not save: ' + str(company) + str(e))
        
    
def generate_vestigingen(number):
    """Generate Vestigingen based on Bedrijven"""
    logger.info("Start loading data for model Vestiging at: " + datetime.now().strftime("%H:%M:%S"))

    companies = Bedrijf.objects.all()

    for i in range(number):
        company = companies.order_by('?').first() 
        vestiging_instance = Vestiging(
            bedrijf = company,
            lattitude=random.uniform(50.765, 53.428456159766675),
            longitude=random.uniform(4.527712777754515, 6.797760069708314),
            vestigingnaam = company.naam + ' vestiging ' + str(i),
            wkk = random.choice([True, False]),
            wkk_2030 = random.choice([True, False]),
        )
        vestiging_instance.save()



def populate_projects(number):
    """Generate random projects"""
    logger.info("Start loading data for model Project at: " + datetime.now().strftime("%H:%M:%S"))
    vestigingen = Vestiging.objects.all()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    length = 10
    for i in range(number):
        
        project_instance = Project(
            vestiging = vestigingen.order_by('?').first(),       
            
            naam=''.join(random.choice(letters) for i in range(length))
        
        )
        project_instance.save()

def generate_project_getallen():
    """Generate random project getallen"""
    projects = Project.objects.all()

    jaar_realisatie_opties = [2025, 2030, 2035, 2040, 2045, 2050]
    for project in projects:
        project_key_figures = Project_kerngetallen(
                project = project,
                aardgas_verandering = [random.randint(0, 100) if random.randint(0,100) > 30 else 0][0],
                biogas_verandering = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                elektriciteit_verandering  = [random.randint(0, 100) if random.randint(0,100) > 20 else 0][0],
                verzwaring_netaansluiting = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                stoom_verandering  = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                overige_warmte_verandering = [random.randint(0, 100) if random.randint(0,100) > 95 else 0][0],
                biomassa_verandering =[random.randint(0, 100) if random.randint(0,100) > 95 else 0][0],
                afval_verandering = [random.randint(0, 100) if random.randint(0,100) > 95 else 0][0],
                waterstof_energie_verandering = [random.randint(0, 100) if random.randint(0,100) > 75 else 0][0],
                productie_verandering =[random.randint(0, 100) if random.randint(0,100) > 95 else 0][0],
                co2_uitstoot_verandering  =[random.randint(0, 100) if random.randint(0,100) > 25 else 0][0],
                nox_uitstoot_verandering  = [random.randint(0, 100) if random.randint(0,100) > 25 else 0][0],
                jaar_realisatie = random.choice(jaar_realisatie_opties), 
                status = Project_kerngetallen.STATUS_OPTIONS[random.randint(0, 2)][0],
                )

        project_key_figures.save()


def populate_energie_import_export():
    vestigingen = Vestiging.objects.all()
    jaaropties = [2000, 2010, 2015, 2020]

    for jaar in jaaropties:
        for vestiging in vestigingen:

            energie_import_instance = Energie_import(
                    vestiging = vestiging,
                    jaar = jaar,
                    aardgas = [random.randint(0, 100) if random.randint(0,100) > 30 else 0][0],
                    biogas = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    elektriciteit = [random.randint(0, 100) if random.randint(0,100) > 20 else 0][0],
                    stoom = [random.randint(0, 100) if random.randint(0,100) > 70 else 0][0],
                    overige_warmte =[random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    biomassa = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    afval =[random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    waterstof = [random.randint(0, 100) if random.randint(0,100) > 80 else 0][0],
                    co2 = [random.randint(0, 100) if random.randint(0,100) > 30 else 0][0],
                )
                
            energie_export_instance = Energie_export(
                    vestiging = vestiging,
                    jaar = jaar,
                    aardgas = [random.randint(0, 100) if random.randint(0,100) > 30 else 0][0],
                    biogas = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    elektriciteit = [random.randint(0, 100) if random.randint(0,100) > 20 else 0][0],
                    stoom = [random.randint(0, 100) if random.randint(0,100) > 70 else 0][0],
                    overige_warmte =[random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    biomassa = [random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    afval =[random.randint(0, 100) if random.randint(0,100) > 90 else 0][0],
                    waterstof = [random.randint(0, 100) if random.randint(0,100) > 80 else 0][0],
                    co2 = [random.randint(0, 100) if random.randint(0,100) > 30 else 0][0],
                )

            energie_import_instance.save()
            energie_export_instance.save()


if __name__ == "__main__":
    logger.setLevel(20)                         ## set logging level [CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10]
    
    generate_bedrijven()
    generate_vestigingen(40)
    populate_projects(100)
    generate_project_getallen()
    populate_energie_import_export()