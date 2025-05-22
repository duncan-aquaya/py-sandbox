"""
Config module for WQAF Kenya Expansion
"""

study_counties = [
    "Nakuru",
    "Uasin Gishu",
    "Kericho",
]

study_labs = [
    "Eldoret Water And Sanitation Company Limited",
    "Nakuru Water and Sanitation Services Company Limited",
    "Kisumu Water and Sanitation Company Limited (KIWASCO)",
]

primary_counties = [
    "Nakuru",
    "Mombasa",
    "Kiambu",
    "Uasin Gishu",
    "Nyeri"
]

secondary_counties = [
    "Kirinyaga",
    "Embu",
    "Nyandarua",
    "Laikipia",
    "Meru",
    "Murang'a",
    "Nandi",
    "Elgeyo-Marakwet",
    "Kilifi",
    "Kwale",
    "Taita Taveta"
]

selected_labs = [
    "Nakuru Water and Sanitation Services Company Limited",
    "Polucon Services Kenya Limited",
    "Crop Nutrition Laboratory Services Limited",
    "Eldoret Water And Sanitation Company Limited",
    "Nyeri Water and Sanitation Company"
]


# UNOCHA COD-PP Data Config
codpp_cols = ['NEWDLAT', 'NEWDLONG', "FULL_NAME", "ADM1", 'DISTRICT', 'REGION', 'LOCATION',
              'SUB_LOCATI', 'geometry']

codpp_county_map = {
    "E. Marakwet": "Elgeyo-Marakwet",
    "Muranga": "Murang'a",
    "Taita Tavet": "Taita Taveta",
}

