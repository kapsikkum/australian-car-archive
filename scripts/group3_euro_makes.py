"""
Group 3: European makes in Australia (23 makes)
"""
from typing import Dict, Any

EURO_MAKES: Dict[str, Dict[str, Any]] = {
    "volkswagen": {
        "make_slug": "volkswagen",
        "name": "Volkswagen",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 1953, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Volkswagen has been a core pillar of Australian motoring for over seven decades, progressing from local CKD assembly of the Beetle and Kombi at Clayton, Victoria to an expansive European passenger and commercial vehicle line-up.",
        "australian_history": "Volkswagen entered the Australian market in 1953 when the first 100 CKD Type 1 Beetles were imported and assembled by Regent Motors and Martin & King in Melbourne. In 1954, Volkswagen (Australasia) Pty Ltd was established, acquiring the former Martin & King factory at Clayton, Victoria. The plant expanded rapidly into full manufacturing with local sheet-metal pressings, engine machining, and paint facilities, reaching over 80% Australian domestic content by 1960. Unique Australian creations were engineered at Clayton, most notably the Volkswagen Country Buggy (Type 197) designed by Rudi Herz in 1967. Facing declining air-cooled sales and high local-content tariffs, Volkswagen sold the Clayton manufacturing facility to Motor Producers Limited (Nissan Australia) in 1968, transitioning to CKD assembly and eventually full CBU importation. After distribution through LNC Industries and Ateco in the 1980s and 1990s, Volkswagen Group Australia (VGA) was founded in 2001. Modern VGA models like the Golf, Polo, Tiguan, Touareg, Amarok utility, and ID electric vehicles have cemented Volkswagen as one of Australia's premier European marques.",
        "models_catalog": [
            {
                "model_slug": "golf",
                "name": "Golf",
                "vehicle_type": "Hatchback / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1976, "end": "Present"},
                "locally_built": True,
                "overview": "The benchmark European small hatchback in Australia across eight generations, from Clayton-assembled Mk1s to iconic GTI and all-wheel-drive R performance flagships.",
                "generations": [
                    {"series_code": "Mk1", "generation_name": "Golf Mark 1 (Typ 17)", "years": {"start": 1976, "end": 1982}, "body_styles": ["3-door hatchback", "5-door hatchback"], "summary": "Assembled locally at Clayton VIC; powered by 1.5L and 1.6L petrol engines and later 1.5L diesel."},
                    {"series_code": "Mk2", "generation_name": "Golf Mark 2 (Typ 19E)", "years": {"start": 1983, "end": 1992}, "body_styles": ["3-door hatchback", "5-door hatchback"], "summary": "Imported in limited numbers, establishing the Australian GTI cult following with the 1.8L 8V engine."},
                    {"series_code": "Mk3", "generation_name": "Golf Mark 3 (Typ 1H)", "years": {"start": 1992, "end": 1998}, "body_styles": ["3-door hatchback", "5-door hatchback", "Convertible"], "summary": "Introduced CL, GL, 2.0L GTI and the iconic 2.8L VR6 narrow-angle six-cylinder."},
                    {"series_code": "Mk4", "generation_name": "Golf Mark 4 (Typ 1J)", "years": {"start": 1998, "end": 2004}, "body_styles": ["5-door hatchback"], "summary": "Elevated interior quality; introduced 1.8T 20V GTI, 2.3L V5, and halo 3.2L VR6 R32 4Motion."},
                    {"series_code": "Mk5", "generation_name": "Golf Mark 5 (Typ 1K)", "years": {"start": 2004, "end": 2009}, "body_styles": ["5-door hatchback", "Wagon"], "summary": "Multi-link rear suspension, DSG dual-clutch transmission, 2.0 TFSI GTI (147kW), TDI diesels, and R32."},
                    {"series_code": "Mk6", "generation_name": "Golf Mark 6 (Typ 5K)", "years": {"start": 2009, "end": 2013}, "body_styles": ["5-door hatchback", "Wagon", "Cabriolet"], "summary": "Refined refinement and acoustics; 118TSI Twincharger, 2.0 TDI, 155kW GTI, and 188kW all-wheel drive Golf R."},
                    {"series_code": "Mk7", "generation_name": "Golf Mark 7 & 7.5 (Typ 5G)", "years": {"start": 2013, "end": 2020}, "body_styles": ["5-door hatchback", "Wagon"], "summary": "MQB platform lightweight architecture, 90TSI/110TSI, 162kW-180kW GTI, and 206kW-213kW Golf R."},
                    {"series_code": "Mk8", "generation_name": "Golf Mark 8 & 8.5 (Typ CD1)", "years": {"start": 2020, "end": "Present"}, "body_styles": ["5-door hatchback", "Wagon"], "summary": "Digital cockpit, 1.4 TSI 8-speed automatic, 180kW GTI, and 235kW Golf R with rear torque-vectoring."}
                ]
            },
            {
                "model_slug": "amarok",
                "name": "Amarok",
                "vehicle_type": "Ute / Pickup Truck",
                "segment": "Mid-size Ute",
                "years_sold_au": {"start": 2011, "end": "Present"},
                "locally_built": False,
                "overview": "Volkswagen's rugged ladder-frame dual-cab and single-cab ute, revered in Australia for permanent 4Motion AWD and muscular 3.0-litre V6 TDI powertrains.",
                "generations": [
                    {"series_code": "2H", "generation_name": "Amarok First Generation", "years": {"start": 2011, "end": 2022}, "body_styles": ["Dual-cab ute", "Single-cab ute"], "summary": "Launched with 2.0 Bi-TDI; elevated to legendary status in 2016 with the 3.0L V6 TDI (up to 200kW overboost) and Walkinshaw W580 tuning."},
                    {"series_code": "T1", "generation_name": "Amarok Second Generation", "years": {"start": 2023, "end": "Present"}, "body_styles": ["Dual-cab ute"], "summary": "Co-developed with Ford on upgraded T6 platform; offered in Core, Life, Style, PanAmericana, and Aventura with 2.0 TDI, 3.0 V6 TDI, and 2.3 TSI turbo petrol."}
                ]
            },
            {
                "model_slug": "beetle",
                "name": "Beetle",
                "vehicle_type": "Sedan / Hatchback / Convertible",
                "segment": "Small Car",
                "years_sold_au": {"start": 1953, "end": 2019},
                "locally_built": True,
                "overview": "The car that founded Volkswagen in Australia, built with high local content at Clayton VIC before evolving into the retro New Beetle and Beetle A5.",
                "generations": [
                    {"series_code": "Type 1", "generation_name": "Beetle Classic", "years": {"start": 1953, "end": 1976}, "body_styles": ["2-door sedan"], "summary": "Assembled at Clayton VIC with 1192cc, 1285cc, 1493cc, and 1584cc air-cooled boxer-four engines, including Super Beetle 1302/1303."},
                    {"series_code": "Typ 9C", "generation_name": "New Beetle", "years": {"start": 2000, "end": 2011}, "body_styles": ["3-door hatchback", "2-door convertible"], "summary": "Golf Mk4-based retro revival featuring 2.0L, 1.8T, and 1.9 TDI engines."},
                    {"series_code": "Typ 5C", "generation_name": "Beetle A5", "years": {"start": 2013, "end": 2019}, "body_styles": ["3-door hatchback"], "summary": "Lower, wider coupe-like silhouette powered by 1.4 TSI twincharged and 2.0 TSI engines."}
                ]
            },
            {
                "model_slug": "kombi-transporter",
                "name": "Kombi / Transporter",
                "vehicle_type": "Van / People Mover",
                "segment": "Light Commercial",
                "years_sold_au": {"start": 1954, "end": "Present"},
                "locally_built": True,
                "overview": "Australia's iconic surf-wagon, delivery van, and camper, assembled at Clayton VIC across T1 and T2 eras, and imported through modern T6.1, T7, and ID.Buzz.",
                "generations": [
                    {"series_code": "T1-T2", "generation_name": "Kombi Splitty & Bay Window", "years": {"start": 1954, "end": 1979}, "body_styles": ["Van", "Camper", "Microbus", "Ute"], "summary": "Assembled at Clayton; became an enduring cultural icon of Australian beach and holiday culture."},
                    {"series_code": "T3-T4", "generation_name": "Transporter / Caravelle T3 & T4", "years": {"start": 1980, "end": 2003}, "body_styles": ["Van", "Caravelle bus"], "summary": "Transitioned from rear-engine boxer to front-engine front-wheel-drive Transporter T4."},
                    {"series_code": "T5-T6", "generation_name": "Transporter / Multivan T5 & T6", "years": {"start": 2004, "end": "Present"}, "body_styles": ["Van", "Crewvan", "Multivan", "California"], "summary": "TDI turbo-diesel powertrains with 4Motion AWD availability and premium Multivan executive shuttles."}
                ]
            },
            {
                "model_slug": "passat",
                "name": "Passat",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Medium / Large Car",
                "years_sold_au": {"start": 1974, "end": "Present"},
                "locally_built": True,
                "overview": "Volkswagen's flagship executive sedan and wagon, originally assembled at Clayton and later imported across B1 through B8 generations and Alltrack rugged wagons.",
                "generations": [
                    {"series_code": "B1-B2", "generation_name": "Passat Mark 1 & 2", "years": {"start": 1974, "end": 1988}, "body_styles": ["Hatchback", "Sedan", "Wagon"], "summary": "Assembled locally in B1 form; later imported as B2 Santana sedan and wagon."},
                    {"series_code": "B5-B6", "generation_name": "Passat Mark 5 & 6", "years": {"start": 1998, "end": 2010}, "body_styles": ["Sedan", "Wagon"], "summary": "Longitudinal then transverse platforms with V6, 2.0T, 3.6 FSI R36 sports wagon, and TDI diesels."},
                    {"series_code": "B7-B8", "generation_name": "Passat Mark 7 & 8", "years": {"start": 2011, "end": "Present"}, "body_styles": ["Sedan", "Wagon", "Alltrack"], "summary": "MQB-based premium executive wagon and high-riding Alltrack 4Motion crossover."}
                ]
            },
            {
                "model_slug": "polo",
                "name": "Polo",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 1996, "end": "Present"},
                "locally_built": False,
                "overview": "Class-leading European light hatchback offering premium interior refinement, TSI turbo efficiency, and fiery Polo GTI hot-hatch models.",
                "generations": [
                    {"series_code": "Mk3-Mk4", "generation_name": "Polo Mark 3 & 4", "years": {"start": 1996, "end": 2009}, "body_styles": ["3-door hatchback", "5-door hatchback"], "summary": "Introduced Polo 1.6L and 1.8T Polo GTI into the Australian light car segment."},
                    {"series_code": "Mk5-Mk6", "generation_name": "Polo Mark 5 & 6", "years": {"start": 2010, "end": "Present"}, "body_styles": ["5-door hatchback"], "summary": "MQB A0 architecture, digital instrumentation, 70TSI/85TSI, and 147kW Polo GTI 2.0 TSI."}
                ]
            },
            {
                "model_slug": "tiguan",
                "name": "Tiguan",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2008, "end": "Present"},
                "locally_built": False,
                "overview": "One of Australia's top-selling European SUVs, spanning 5-seat Tiguan, 7-seat Tiguan Allspace, and 235kW Tiguan R flagship.",
                "generations": [
                    {"series_code": "5N", "generation_name": "Tiguan First Generation", "years": {"start": 2008, "end": 2016}, "body_styles": ["5-door SUV"], "summary": "Golf Mk5-based compact SUV with 125TSI, 147TSI, and 103TDI 4Motion."},
                    {"series_code": "AD-BW", "generation_name": "Tiguan Second Generation", "years": {"start": 2016, "end": "Present"}, "body_styles": ["5-door SUV", "7-door Allspace"], "summary": "MQB platform 110TSI, 132TSI, 162TSI Highline, Allspace long-wheelbase, and 235kW Tiguan R."}
                ]
            },
            {
                "model_slug": "touareg",
                "name": "Touareg",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Full-size luxury off-road SUV famous in Australia for 3,500kg towing and powerhouse V6, V10 TDI, and V8 TDI powertrains.",
                "generations": [
                    {"series_code": "7L", "generation_name": "Touareg First Generation", "years": {"start": 2003, "end": 2010}, "body_styles": ["5-door SUV"], "summary": "Dual-range transfer case, air suspension, 3.2 V6, 3.0 V6 TDI, and legendary 5.0L V10 TDI."},
                    {"series_code": "7P-CR", "generation_name": "Touareg 2nd & 3rd Gen", "years": {"start": 2011, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "MLB Evo platform sharing with Audi Q7/Porsche Cayenne, 170TDI/210TDI V6, and 340kW Touareg R PHEV."}
                ]
            }
        ]
    },
    "bmw": {
        "make_slug": "bmw",
        "name": "BMW",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 1960, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The Ultimate Driving Machine in Australia, renowned for sports sedans, touring car dominance at Mount Panorama, and pioneering luxury X-series SUVs.",
        "australian_history": "BMW vehicles were first imported to Australia by independent distributors such as Capitol Motors in Sydney and Ron Hodgson in the 1960s. In 1979, BMW Australia Pty Ltd was established as a wholly owned subsidiary based in Mulgrave, Victoria. BMW built immense Australian sporting credibility through motorsport: Frank Gardner's JPS Team BMW dominated the Australian Touring Car Championship (ATCC) in the 1980s with Jim Richards driving the sleek black-and-gold 635CSi (1985 ATCC winner) and E30 M3 (1987 ATCC winner). Tony Longhurst and Richards claimed the Bathurst 1000 in 1991 and 1992 in Class B with M3s. Australia quickly became one of BMW's highest-penetration markets globally for M performance vehicles and X-series Sports Activity Vehicles, with models like the 3 Series, 5 Series, X3, and X5 maintaining top-tier status.",
        "models_catalog": [
            {
                "model_slug": "3-series",
                "name": "3 Series",
                "vehicle_type": "Sedan / Coupe / Wagon / Convertible",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1976, "end": "Present"},
                "locally_built": False,
                "overview": "The benchmark luxury sports sedan in Australia across seven generations from E21 to G20, including legendary M3 high-performance iterations.",
                "generations": [
                    {"series_code": "E21", "generation_name": "3 Series E21", "years": {"start": 1976, "end": 1983}, "body_styles": ["2-door sedan"], "summary": "Pioneered the compact executive sports sedan with 318, 320, and fuel-injected 323i inline-six."},
                    {"series_code": "E30", "generation_name": "3 Series E30", "years": {"start": 1983, "end": 1991}, "body_styles": ["2-door sedan", "4-door sedan", "Convertible", "Touring"], "summary": "Cult classic in Australia; 318i, 320i, 323i, 325i, and Group A homologation M3 with S14 2.3L."},
                    {"series_code": "E36", "generation_name": "3 Series E36", "years": {"start": 1991, "end": 1998}, "body_styles": ["4-door sedan", "2-door coupe", "Convertible", "Compact", "Touring"], "summary": "Z-axle multi-link rear suspension, 318is, 325i, 328i, and 3.0L/3.2L M3 (up to 236kW)."},
                    {"series_code": "E46", "generation_name": "3 Series E46", "years": {"start": 1998, "end": 2006}, "body_styles": ["4-door sedan", "2-door coupe", "Convertible", "Touring", "Compact"], "summary": "Widely regarded as design peak; 318i to 330i, and iconic 252kW M3 with high-revving S54 3.2L inline-six."},
                    {"series_code": "E90", "generation_name": "3 Series E90 / E92", "years": {"start": 2005, "end": 2012}, "body_styles": ["4-door sedan", "2-door coupe", "Convertible", "Touring"], "summary": "Run-flat tyres, iDrive, twin-turbo 335i (N54/N55), and 309kW 4.0L S65 V8 M3."},
                    {"series_code": "F30", "generation_name": "3 Series F30", "years": {"start": 2012, "end": 2019}, "body_styles": ["4-door sedan", "Touring"], "summary": "Turbocharged 4-cylinder and inline-6 (320i, 328i, 330i, 340i B58) and twin-turbo S55 M3."},
                    {"series_code": "G20", "generation_name": "3 Series G20", "years": {"start": 2019, "end": "Present"}, "body_styles": ["4-door sedan", "Touring"], "summary": "Stiffer CLAR architecture, 320i, 330i, M340i xDrive (285kW), M3 (353kW/375kW), and M3 Touring."}
                ]
            },
            {
                "model_slug": "5-series",
                "name": "5 Series",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1973, "end": "Present"},
                "locally_built": False,
                "overview": "BMW's executive express, defining executive sports saloons from E12 and E28 through E39 and modern G60.",
                "generations": [
                    {"series_code": "E12-E28", "generation_name": "5 Series E12 & E28", "years": {"start": 1973, "end": 1988}, "body_styles": ["4-door sedan"], "summary": "Established BMW's 6-cylinder executive dominance; 520, 528i, 535i, and first M5."},
                    {"series_code": "E34-E39", "generation_name": "5 Series E34 & E39", "years": {"start": 1988, "end": 2003}, "body_styles": ["4-door sedan", "Touring"], "summary": "E39 considered benchmark executive chassis; 523i, 528i, 540i V8, and 294kW S62 V8 M5."},
                    {"series_code": "E60-F10-G30", "generation_name": "5 Series E60, F10 & G30", "years": {"start": 2003, "end": "Present"}, "body_styles": ["4-door sedan", "Touring"], "summary": "V10 M5 (S85 373kW), twin-turbo V8 M5, and modern mild-hybrid/i5 electric G60."}
                ]
            },
            {
                "model_slug": "x5",
                "name": "X5",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2000, "end": "Present"},
                "locally_built": False,
                "overview": "Pioneered the performance luxury SUV in Australia, delivering car-like road dynamics and immense prestige.",
                "generations": [
                    {"series_code": "E53", "generation_name": "X5 First Generation", "years": {"start": 2000, "end": 2006}, "body_styles": ["5-door SUV"], "summary": "Transformed Australian luxury SUV market with 3.0i, 4.4i, 4.6is, and 3.0d turbo diesel."},
                    {"series_code": "E70-F15", "generation_name": "X5 2nd & 3rd Gen", "years": {"start": 2007, "end": 2018}, "body_styles": ["5-door SUV"], "summary": "Optional 7 seats, xDrive AWD, 30d, 40d, tri-turbo M50d, and twin-turbo V8 X5 M."},
                    {"series_code": "G05", "generation_name": "X5 Fourth Generation", "years": {"start": 2019, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "CLAR platform xDrive30d, xDrive40i, xDrive50e PHEV, M60i V8, and 460kW X5 M Competition."}
                ]
            },
            {
                "model_slug": "m3",
                "name": "M3",
                "vehicle_type": "Coupe / Sedan / Wagon",
                "segment": "Sports Performance",
                "years_sold_au": {"start": 1987, "end": "Present"},
                "locally_built": False,
                "overview": "The iconic high-performance sports benchmark in Australia with ATCC championship victories and high-revving motorsport powertrains.",
                "generations": [
                    {"series_code": "E30-E36", "generation_name": "M3 E30 & E36", "years": {"start": 1987, "end": 1999}, "body_styles": ["Coupe", "Sedan", "Convertible"], "summary": "E30 2.3L 4-cylinder touring car hero; E36 3.0L (210kW) and 3.2L (236kW) inline-six."},
                    {"series_code": "E46-E90", "generation_name": "M3 E46 & E90/E92", "years": {"start": 2001, "end": 2013}, "body_styles": ["Coupe", "Sedan", "Convertible"], "summary": "E46 252kW S54 screamers (including lightweight CSL); E90/92 with 309kW 4.0L S65 V8."},
                    {"series_code": "F80-G80", "generation_name": "M3 F80 & G80", "years": {"start": 2014, "end": "Present"}, "body_styles": ["Sedan", "Touring"], "summary": "Twin-turbo S55 (F80) and S58 (G80 up to 405kW CS), introducing M xDrive and M3 Touring."}
                ]
            }
        ]
    },
    "mercedes-benz": {
        "make_slug": "mercedes-benz",
        "name": "Mercedes-Benz",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 1958, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "The gold standard of luxury, safety, and performance in Australia, distinguished by historic local CKD assembly in Port Melbourne and world-leading AMG performance sales.",
        "australian_history": "Mercedes-Benz cars arrived in Australia in the early 20th century, but formal operations surged in 1958 when Mercedes-Benz (Australia) Pty Ltd was formed in partnership with Standard-Vacuum and Australian Motor Industries (AMI). From 1959 to 1965, Mercedes-Benz passenger cars—specifically the W120/W121 'Ponton' 190 and W110/W111 'Fintail' 220 and 220S—were assembled at AMI's factory in Port Melbourne, Victoria. Australia was one of the very few countries outside Germany to assemble Mercedes-Benz passenger cars. Local assembly concluded in 1965 as Daimler-Benz AG assumed full control of imports and distribution, establishing its headquarters in Mulgrave, Victoria. Mercedes-Benz pioneered automotive safety introductions in Australia, including crumple zones, anti-lock brakes (ABS in 1978), and electronic stability control (ESP). Australia also boasts one of the highest per-capita sales of Mercedes-AMG performance vehicles anywhere in the world, with models like the C63 AMG attaining legendary status.",
        "models_catalog": [
            {
                "model_slug": "c-class",
                "name": "C-Class",
                "vehicle_type": "Sedan / Wagon / Coupe / Convertible",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1994, "end": "Present"},
                "locally_built": False,
                "overview": "Mercedes-Benz's top-selling luxury model line in Australia across W202, W203, W204, W205, and W206, celebrated for safety, comfort, and thundering AMG V8 variants.",
                "generations": [
                    {"series_code": "W202", "generation_name": "C-Class W202", "years": {"start": 1994, "end": 2000}, "body_styles": ["4-door sedan", "Estate wagon"], "summary": "Replaced the 190E (W201); Classic, Elegance, Sport trims, C180 to C280, and C36/C43 AMG V8."},
                    {"series_code": "W203", "generation_name": "C-Class W203", "years": {"start": 2000, "end": 2007}, "body_styles": ["4-door sedan", "Estate wagon", "Sports Coupe"], "summary": "Distinctive twin-oval headlamps, C180K, C200K, C320, C32 AMG supercharged V6, and C55 AMG 5.4L V8."},
                    {"series_code": "W204", "generation_name": "C-Class W204", "years": {"start": 2007, "end": 2014}, "body_styles": ["4-door sedan", "Estate wagon", "2-door coupe"], "summary": "Agility Control, C200 CGI, C250, C300, and iconic naturally aspirated 6.2L M156 V8 C63 AMG."},
                    {"series_code": "W205", "generation_name": "C-Class W205", "years": {"start": 2014, "end": 2021}, "body_styles": ["4-door sedan", "Estate wagon", "Coupe", "Cabriolet"], "summary": "MRA platform lightweight body, C200, C300, twin-turbo V6 C43, and 375kW 4.0L Biturbo V8 C63 S."},
                    {"series_code": "W206", "generation_name": "C-Class W206", "years": {"start": 2021, "end": "Present"}, "body_styles": ["4-door sedan", "Estate wagon"], "summary": "S-Class inspired interior with 11.9-inch portrait screen, mild-hybrid C200/C300, and 500kW C63 S E Performance."}
                ]
            },
            {
                "model_slug": "e-class",
                "name": "E-Class",
                "vehicle_type": "Sedan / Wagon / Coupe / Convertible",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1959, "end": "Present"},
                "locally_built": True,
                "overview": "The heart of Mercedes-Benz luxury and engineering durability, originally assembled at Port Melbourne (W110/W111) and progressing through W123, W124, to modern W214.",
                "generations": [
                    {"series_code": "W110-W114-W123", "generation_name": "Classic E-Class Ancestors", "years": {"start": 1959, "end": 1985}, "body_styles": ["4-door sedan", "Estate wagon", "Coupe"], "summary": "W110/W111 assembled at AMI Port Melbourne; indestructible W123 230E, 280E, and 300D."},
                    {"series_code": "W124-W210-W211", "generation_name": "E-Class W124, W210 & W211", "years": {"start": 1986, "end": 2009}, "body_styles": ["Sedan", "Wagon", "Coupe", "Convertible"], "summary": "Over-engineered W124; twin-headlight W210; supercharged E55 AMG and 6.2L E63 AMG W211."},
                    {"series_code": "W212-W213-W214", "generation_name": "Modern E-Class", "years": {"start": 2009, "end": "Present"}, "body_styles": ["Sedan", "Wagon", "Coupe", "Cabriolet"], "summary": "Advanced driver assistance, 4Matic AWD, E300, E350, and 450kW twin-turbo V8 E63 S."}
                ]
            },
            {
                "model_slug": "s-class",
                "name": "S-Class",
                "vehicle_type": "Sedan / Coupe",
                "segment": "Upper Luxury Car",
                "years_sold_au": {"start": 1972, "end": "Present"},
                "locally_built": False,
                "overview": "The undisputed flagship of automotive innovation in Australia, introducing world-first safety and luxury technologies on W116, W126, W140, W220, W221, W222, and W223.",
                "generations": [
                    {"series_code": "W116-W126", "generation_name": "S-Class W116 & W126", "years": {"start": 1972, "end": 1991}, "body_styles": ["4-door sedan", "Coupe"], "summary": "W116 introduced ABS and 450SEL 6.9; Bruno Sacco's timeless W126 with airbags and 560SEL V8."},
                    {"series_code": "W140-W220-W221", "generation_name": "S-Class W140, W220 & W221", "years": {"start": 1992, "end": 2013}, "body_styles": ["4-door sedan", "Coupe"], "summary": "Double-glazed W140 'Cathedral'; Airmatic W220; Night View Assist and bi-turbo V8/V12 W221."},
                    {"series_code": "W222-W223", "generation_name": "Modern S-Class", "years": {"start": 2014, "end": "Present"}, "body_styles": ["4-door sedan", "Coupe", "Maybach"], "summary": "Magic Body Control, rear-axle steering, Level 3 Drive Pilot, and ultra-luxurious Mercedes-Maybach."}
                ]
            },
            {
                "model_slug": "g-class",
                "name": "G-Class",
                "vehicle_type": "Off-road SUV",
                "segment": "Heavy Off-Road / Luxury SUV",
                "years_sold_au": {"start": 1982, "end": "Present"},
                "locally_built": False,
                "overview": "The Geländewagen legend, serving with the Australian Defence Force as tactical 4x4 and 6x6 fleet, and ruling city streets as the ultra-luxury G63 AMG.",
                "generations": [
                    {"series_code": "W460-W461", "generation_name": "G-Class Utility & Military", "years": {"start": 1982, "end": 2018}, "body_styles": ["Station wagon", "Cab-chassis", "6x6"], "summary": "Triple locking differentials; selected for Project Overlander by Australian Army (over 2,000 ADF vehicles)."},
                    {"series_code": "W463", "generation_name": "G-Class W463 & Modern G63", "years": {"start": 2000, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Independent front suspension redesign in 2018, twin-turbo 4.0L V8 G63 AMG (430kW), and all-electric G580 EQ."}
                ]
            }
        ]
    },
    "audi": {
        "make_slug": "audi",
        "name": "Audi",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 1968, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Audi represents Vorsprung durch Technik in Australia, celebrated for quattro all-wheel drive, RS performance estates, and high-tech luxury SUVs.",
        "australian_history": "Audi entered the Australian market in the late 1960s with models like the Audi Super 90 and 100 sold through Volkswagen dealers. Distribution transitioned through LNC Industries and Ateco Automotive until Audi Australia Pty Ltd was established in 1997. Audi's Australian breakthrough accelerated in the 2000s under managing director Joerg Hofmann, who expanded the national dealer network and established the brand as a core German luxury rival to BMW and Mercedes-Benz. Audi's motorsport triumphs at Mount Panorama—including back-to-back Bathurst 12 Hour victories with the Audi R8 LMS GT3 in 2011 and 2012—cemented its high-performance reputation. Models like the A4, A3, Q5, Q7, and RS performance flagships (RS3, RS4, RS6 Avant) remain Australian automotive favorites.",
        "models_catalog": [
            {
                "model_slug": "a4",
                "name": "A4",
                "vehicle_type": "Sedan / Avant Wagon / Allroad",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1995, "end": "Present"},
                "locally_built": False,
                "overview": "Audi's core luxury sedan and Avant wagon, pioneering quattro all-wheel drive in the compact executive class across B5 through B9.",
                "generations": [
                    {"series_code": "B5-B6", "generation_name": "A4 B5 & B6", "years": {"start": 1995, "end": 2005}, "body_styles": ["Sedan", "Avant wagon"], "summary": "Replaced Audi 80; introduced 1.8 20V, 1.8T quattro, 2.8 V6, S4 2.7 biturbo, and 4.2 V8 B6 S4."},
                    {"series_code": "B7-B8", "generation_name": "A4 B7 & B8", "years": {"start": 2005, "end": 2015}, "body_styles": ["Sedan", "Avant", "Allroad"], "summary": "Singleframe grille, 2.0 TFSI, 3.0 TDI, high-revving 4.2L V8 RS4 (309kW), and MLB platform B8."},
                    {"series_code": "B9", "generation_name": "A4 B9", "years": {"start": 2016, "end": "Present"}, "body_styles": ["Sedan", "Avant", "Allroad"], "summary": "Virtual Cockpit, 35/40/45 TFSI, 2.9L twin-turbo V6 RS4 Avant (331kW / 600Nm)."}
                ]
            },
            {
                "model_slug": "q5",
                "name": "Q5",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2009, "end": "Present"},
                "locally_built": False,
                "overview": "Audi's top-selling vehicle in Australia, revered by families for its refined quattro dynamics, TDI torque, and high-performance SQ5 variant.",
                "generations": [
                    {"series_code": "8R", "generation_name": "Q5 First Generation", "years": {"start": 2009, "end": 2017}, "body_styles": ["5-door SUV"], "summary": "MLB architecture, 2.0 TFSI, 3.0 TDI, and wildly popular twin-turbo diesel SQ5 TDI (230kW / 650Nm)."},
                    {"series_code": "FY", "generation_name": "Q5 Second Generation", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door SUV", "Sportback"], "summary": "Quattro with ultra technology, 40 TDI, 45 TFSI, Sportback coupe silhouette, and SQ5 3.0 TDI."}
                ]
            },
            {
                "model_slug": "rs6-avant",
                "name": "RS6 Avant",
                "vehicle_type": "Wagon",
                "segment": "High Performance Luxury",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "The ultimate high-performance family supercar wagon in Australia, featuring twin-turbo V8 and V10 power with quattro traction.",
                "generations": [
                    {"series_code": "C5-C6", "generation_name": "RS6 C5 & C6", "years": {"start": 2003, "end": 2010}, "body_styles": ["Sedan", "Avant wagon"], "summary": "C5 4.2L twin-turbo V8 (331kW); C6 monumental 5.0L twin-turbo V10 (426kW / 650Nm)."},
                    {"series_code": "C7-C8", "generation_name": "RS6 C7 & C8", "years": {"start": 2013, "end": "Present"}, "body_styles": ["Avant wagon"], "summary": "4.0L twin-turbo V8 producing up to 463kW (630hp) in RS6 Performance with flared widebody."}
                ]
            }
        ]
    },
    "porsche": {
        "make_slug": "porsche",
        "name": "Porsche",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 1951, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The pre-eminent German sports car manufacturer, with Australia holding the distinction of being Porsche's very first right-hand-drive market in the world.",
        "australian_history": "Australia occupies a revered position in Porsche's global history. In 1951, Australian entrepreneur Norman Hamilton traveled to Gmünd and Stuttgart, meeting Ferry Porsche and securing the franchise to import the very first right-hand-drive Porsche 356 models in the world. The first two cars—a Fish Silver Grey 356 Coupe and Cabriolet—arrived in Melbourne in late 1951. Hamilton founded Porsche Cars Australia, operating out of South Melbourne. In 1992, Porsche AG acquired the distributorship directly. Australia became a stronghold for Porsche Carrera Cup racing and sports car sales, with the 911, Boxster, Cayman, Cayenne, Macan, and all-electric Taycan enjoying passionate support.",
        "models_catalog": [
            {
                "model_slug": "911",
                "name": "911",
                "vehicle_type": "Coupe / Cabriolet / Targa",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1964, "end": "Present"},
                "locally_built": False,
                "overview": "The timeless rear-engine sports car icon in Australia, from early air-cooled 2.0-litre flat-sixes to water-cooled twin-turbo Carrera, Turbo, and GT3 track masters.",
                "generations": [
                    {"series_code": "Classic-G-Series", "generation_name": "911 Classic & G-Series", "years": {"start": 1964, "end": 1989}, "body_styles": ["Coupe", "Targa", "Cabriolet"], "summary": "Air-cooled 2.0L to 3.2L Carrera, including the legendary 1973 2.7 Carrera RS and 930 911 Turbo."},
                    {"series_code": "964-993", "generation_name": "911 964 & 993", "years": {"start": 1989, "end": 1998}, "body_styles": ["Coupe", "Targa", "Cabriolet"], "summary": "964 introduced Carrera 4 AWD and Tiptronic; 993 marked the final and celebrated air-cooled era."},
                    {"series_code": "996-997", "generation_name": "911 996 & 997", "years": {"start": 1998, "end": 2012}, "body_styles": ["Coupe", "Cabriolet", "Targa"], "summary": "Water-cooled flat-six, Carrera, Turbo, GT3, and GT2; 997 introduced direct fuel injection and PDK."},
                    {"series_code": "991-992", "generation_name": "911 991 & 992", "years": {"start": 2012, "end": "Present"}, "body_styles": ["Coupe", "Cabriolet", "Targa"], "summary": "Aluminium-steel hybrid chassis, 3.0 twin-turbo flat-six, 992 GT3 with double-wishbone front suspension, and T-Hybrid."}
                ]
            },
            {
                "model_slug": "cayenne",
                "name": "Cayenne",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "The performance luxury SUV that secured Porsche's financial future, delivering authentic sports car dynamics and serious off-road capability in Australia.",
                "generations": [
                    {"series_code": "9PA-92A", "generation_name": "Cayenne 1st & 2nd Gen", "years": {"start": 2003, "end": 2017}, "body_styles": ["5-door SUV"], "summary": "Dual-range transfer case 955/957 with 4.5/4.8 V8 Turbo; 958 lighter architecture with GTS and Turbo S."},
                    {"series_code": "9Y0", "generation_name": "Cayenne Third Generation", "years": {"start": 2018, "end": "Present"}, "body_styles": ["5-door SUV", "Coupe"], "summary": "MLB Evo platform, rear-axle steering, 48V roll stabilization, E-Hybrid, and 471kW Turbo GT Coupe."}
                ]
            },
            {
                "model_slug": "macan",
                "name": "Macan",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2014, "end": "Present"},
                "locally_built": False,
                "overview": "Porsche's best-selling model in Australia, blending everyday practical crossover dimensions with genuine sports car handling.",
                "generations": [
                    {"series_code": "95B", "generation_name": "Macan ICE Generation", "years": {"start": 2014, "end": 2024}, "body_styles": ["5-door SUV"], "summary": "Macan 2.0T, Macan S (3.0 V6), GTS, and Turbo (2.9 twin-turbo V6 producing up to 324kW)."},
                    {"series_code": "Macan-EV", "generation_name": "Macan Electric (PPE)", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "PPE 800V all-electric architecture, Macan 4 and Macan Turbo with up to 470kW overboost."}
                ]
            }
        ]
    },
    "opel": {
        "make_slug": "opel",
        "name": "Opel",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 2012, "end": 2013},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "General Motors' German brand had an extensive presence in Australia rebadged as Holdens (Astra, Barina, Vectra, Calibra, Insignia), but operated briefly as an independent marque from 2012 to 2013.",
        "australian_history": "While Opel vehicles were sold in Australia for decades under the Holden brand—forming the foundation of the Holden Barina (Corsa B/C), Astra (TR, TS, AH), Vectra (JR, JS, ZC), Calibra, and Zafira—General Motors decided in 2011 to launch Opel as a standalone retail brand in Australia. In August 2012, Opel Australia opened with 17 dedicated dealerships, offering the Corsa, Astra, and Insignia, including high-performance OPC models. However, severe price competition, high import costs, and unfavourable currency exchange rates undermined the business case. On 2 August 2013, just one year after launch and after selling only 1,530 vehicles, GM abruptly shuttered Opel Australia.",
        "models_catalog": [
            {
                "model_slug": "astra",
                "name": "Astra",
                "vehicle_type": "Hatchback / Wagon / Coupe",
                "segment": "Small Car",
                "years_sold_au": {"start": 2012, "end": 2013},
                "locally_built": False,
                "overview": "Sold in 5-door hatchback, Sports Tourer wagon, 3-door GTC coupe, and fire-breathing 206kW Astra OPC hot hatch.",
                "generations": [
                    {"series_code": "Astra-J", "generation_name": "Astra J", "years": {"start": 2012, "end": 2013}, "body_styles": ["5-door hatchback", "Sports Tourer wagon", "3-door GTC"], "summary": "Powered by 1.4L Turbo, 1.6L Turbo, 2.0 CDTI, and 206kW/400Nm 2.0L Turbo OPC."}
                ]
            },
            {
                "model_slug": "corsa",
                "name": "Corsa",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 2012, "end": 2013},
                "locally_built": False,
                "overview": "German light car offered in 3-door, 5-door, and 141kW Corsa OPC pocket rocket.",
                "generations": [
                    {"series_code": "Corsa-D", "generation_name": "Corsa D", "years": {"start": 2012, "end": 2013}, "body_styles": ["3-door hatchback", "5-door hatchback"], "summary": "1.4L naturally aspirated engine and 1.6L Turbo OPC with Recaro shell seats."}
                ]
            },
            {
                "model_slug": "insignia",
                "name": "Insignia",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Medium Car",
                "years_sold_au": {"start": 2012, "end": 2013},
                "locally_built": False,
                "overview": "Mid-size German sedan and Sports Tourer wagon, crowned by the 2.8L twin-scroll turbo V6 AWD Insignia OPC.",
                "generations": [
                    {"series_code": "Insignia-A", "generation_name": "Insignia A", "years": {"start": 2012, "end": 2013}, "body_styles": ["4-door sedan", "Sports Tourer wagon"], "summary": "Offered in 2.0 Turbo petrol, 2.0 CDTI diesel, and 239kW Insignia OPC with adaptive 4x4."}
                ]
            }
        ]
    },
    "smart": {
        "make_slug": "smart",
        "name": "Smart",
        "country_of_origin": "Germany",
        "years_active_au": {"start": 2003, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Daimler's micro-car pioneer, introduced to Australia in 2003 with the City-Coupé, Fortwo, and Roadster, and reborn in 2024 as an all-electric premium compact SUV brand.",
        "australian_history": "Smart was launched in Australia in 2003 by DaimlerChrysler Australia with the revolutionary rear-engine City-Coupé (later renamed Fortwo), followed by the cheeky Smart Roadster and 4-seat Forfour. Its ultra-compact 2.5-metre length allowed perpendicular parking in urban Australian metropolises. While acclaimed for design and novelty, low sales and automated-manual transmission criticisms led to its withdrawal from Australia in 2015. In 2024, Smart returned to the Australian market under the joint venture between Mercedes-Benz and Geely, distributed by LSH Auto, as a purveyor of premium electric SUVs including the Smart #1 and Smart #3.",
        "models_catalog": [
            {
                "model_slug": "fortwo",
                "name": "Fortwo / City-Coupé",
                "vehicle_type": "Micro Car",
                "segment": "City Car",
                "years_sold_au": {"start": 2003, "end": "2015"},
                "locally_built": False,
                "overview": "The two-seat city car built around the rigid Tridion safety cell with interchangeable plastic body panels.",
                "generations": [
                    {"series_code": "W450-W451", "generation_name": "Fortwo 1st & 2nd Gen", "years": {"start": 2003, "end": 2015}, "body_styles": ["2-door coupe", "2-door cabriolet"], "summary": "Powered by 698cc turbo and 1.0L 3-cylinder engines with automated manual gearboxes."}
                ]
            },
            {
                "model_slug": "smart-1",
                "name": "#1",
                "vehicle_type": "SUV",
                "segment": "Compact Electric SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Smart's comeback electric crossover in Australia, offering 66kWh battery, 200kW rear-wheel drive, and 315kW dual-motor Brabus flagship.",
                "generations": [
                    {"series_code": "HX11", "generation_name": "Smart #1", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "SEA architecture, Pro+, Premium, and Brabus performance AWD."}
                ]
            }
        ]
    },
    "skoda": {
        "make_slug": "skoda",
        "name": "Škoda",
        "country_of_origin": "Czech Republic",
        "years_active_au": {"start": 1950, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Czech automotive excellence under the Volkswagen Group, celebrated in Australia for 'Simply Clever' packaging, cavernous wagon space, and value-packed Octavia RS performance.",
        "australian_history": "Škoda vehicles were first sold in Australia in the 1950s and 1960s through independent distributors, offering the rear-engine 1000MB and front-engine Octavia. The brand was formally relaunched in October 2007 by Volkswagen Group Australia (VGA). Škoda positioned itself as the smart, practical alternative to mainstream Japanese and German rivals, delivering Volkswagen Group MQB platforms, turbocharged engines, and DSG gearboxes with added practicality and standard equipment. The Octavia RS quickly became an Australian cult performance hero, accounting for nearly 40% of all Octavia sales in Australia. Škoda expanded its footprint with family SUVs like the Yeti, Karoq, and 7-seat Kodiaq.",
        "models_catalog": [
            {
                "model_slug": "octavia",
                "name": "Octavia",
                "vehicle_type": "Liftback / Wagon",
                "segment": "Medium Car",
                "years_sold_au": {"start": 2007, "end": "Present"},
                "locally_built": False,
                "overview": "Škoda's core nameplate in Australia, renowned for massive boot capacities and the beloved Octavia RS performance wagon.",
                "generations": [
                    {"series_code": "1Z", "generation_name": "Octavia Second Generation", "years": {"start": 2007, "end": 2013}, "body_styles": ["5-door liftback", "Estate wagon"], "summary": "Golf Mk5/6 platform; 1.8 TSI, 2.0 TDI, Scout 4x4, and 147kW petrol / 125kW diesel RS."},
                    {"series_code": "5E-NX", "generation_name": "Octavia 3rd & 4th Gen", "years": {"start": 2013, "end": "Present"}, "body_styles": ["Liftback", "Estate wagon"], "summary": "MQB architecture, 110TSI, 140TSI, and 180kW 2.0 TSI Octavia RS with VAQ limited-slip differential."}
                ]
            },
            {
                "model_slug": "kodiaq",
                "name": "Kodiaq",
                "vehicle_type": "SUV",
                "segment": "Large 7-seat SUV",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "A benchmark family 7-seat SUV in Australia, offering 132TSI/140TSI 4x4 versatility and twin-turbo diesel / 180kW 2.0 TSI Kodiaq RS.",
                "generations": [
                    {"series_code": "NS7-PS7", "generation_name": "Kodiaq 1st & 2nd Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door 7-seat SUV"], "summary": "Style, SportLine, and RS with progressive steering, Canton audio, and sliding second row."}
                ]
            }
        ]
    },
    "cupra": {
        "make_slug": "cupra",
        "name": "Cupra",
        "country_of_origin": "Spain",
        "years_active_au": {"start": 2022, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "SEAT's performance-oriented, design-led Spanish brand, launching Australia as its very first market expansion outside Europe in 2022.",
        "australian_history": "In mid-2022, Volkswagen Group launched Cupra in Australia, marking the brand's first global expansion beyond the European continent. Operating an agency direct-to-consumer sales model with stylish Cupra City Garages in Sydney, Melbourne, Brisbane, and Perth, the brand targeted progressive, design-focused buyers. The initial line-up comprised the bespoke Formentor crossover, Leon hot hatchback, and Ateca SUV, available in potent VZx configurations with 228kW 2.0 TSI engines and all-wheel drive. Cupra followed with the all-electric Born hatchback in 2023 and introduced plug-in hybrid VZe models.",
        "models_catalog": [
            {
                "model_slug": "formentor",
                "name": "Formentor",
                "vehicle_type": "Crossover SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Cupra's bespoke crossover coupe, combining striking copper accents with 228kW all-wheel drive performance.",
                "generations": [
                    {"series_code": "KM7", "generation_name": "Formentor", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door crossover"], "summary": "Offered in V, VZ, VZe PHEV, and 228kW/400Nm VZx AWD with Brembo brake option."}
                ]
            },
            {
                "model_slug": "born",
                "name": "Born",
                "vehicle_type": "Hatchback",
                "segment": "Electric Small Car",
                "years_sold_au": {"start": 2023, "end": "Present"},
                "locally_built": False,
                "overview": "Cupra's first all-electric hot hatch in Australia, featuring rear-wheel drive and up to 170kW e-Boost performance.",
                "generations": [
                    {"series_code": "K11", "generation_name": "Born", "years": {"start": 2023, "end": "Present"}, "body_styles": ["5-door hatchback"], "summary": "MEB platform, 77kWh usable battery, 511km range, rear-motor RWD with e-Boost."}
                ]
            }
        ]
    },
    "seat": {
        "make_slug": "seat",
        "name": "SEAT",
        "country_of_origin": "Spain",
        "years_active_au": {"start": 1995, "end": 1999},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Spanish marque distributed in Australia during the late 1990s by Ateco Automotive, offering Volkswagen-engineered hatchbacks and sedans.",
        "australian_history": "SEAT entered the Australian market in 1995 through independent distributor Ateco Automotive. Pitching European Mediterranean flair with German mechanicals (Polo and Golf platforms), SEAT offered the Ibiza hatchback, Cordoba sedan, and Toledo hatch. In 1999, Volkswagen Group assumed distribution rights, but due to brand overlap with VW and small sales volumes (around 3,000 units sold overall), SEAT withdrew from Australia at the end of 1999.",
        "models_catalog": [
            {
                "model_slug": "ibiza",
                "name": "Ibiza",
                "vehicle_type": "Hatchback",
                "segment": "Light Car",
                "years_sold_au": {"start": 1995, "end": 1999},
                "locally_built": False,
                "overview": "Volkswagen Polo-based light hatchback offered in 1.6L, 1.8L, and 2.0L GTi configurations.",
                "generations": [
                    {"series_code": "6K", "generation_name": "Ibiza Second Generation", "years": {"start": 1995, "end": 1999}, "body_styles": ["3-door hatchback", "5-door hatchback"], "summary": "Designed by Giorgetto Giugiaro; offered in CLX, GLX, and 85kW/110kW GTi 16V."}
                ]
            },
            {
                "model_slug": "cordoba",
                "name": "Cordoba",
                "vehicle_type": "Sedan",
                "segment": "Small Car",
                "years_sold_au": {"start": 1995, "end": 1999},
                "locally_built": False,
                "overview": "Booted four-door sedan sibling of the Ibiza, offering impressive luggage space.",
                "generations": [
                    {"series_code": "6K", "generation_name": "Cordoba First Generation", "years": {"start": 1995, "end": 1999}, "body_styles": ["4-door sedan"], "summary": "Powered by 1.6L and 1.8L four-cylinder engines."}
                ]
            }
        ]
    },
    "volvo": {
        "make_slug": "volvo",
        "name": "Volvo",
        "country_of_origin": "Sweden",
        "years_active_au": {"start": 1960, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Renowned worldwide for safety innovation and in Australia for local assembly of the 140/240 series, Bathurst-winning touring cars, and rapid transition to electrified SUVs.",
        "australian_history": "Volvo began selling in Australia in the 1960s and established Volvo Australia Pty Ltd in 1970. Between 1970 and 1989, Volvo passenger cars—including the 144, 164, 240, and 264—were assembled in Australia, first at Motor Producers Limited (Clayton, VIC) and later at Volvo's dedicated assembly plant in Wacol, Brisbane (QLD). The robust 240 series became an indelible part of Australian family life. Volvo also etched its name into Australian motorsport folklore: Robbie Francevic won the 1986 Australian Touring Car Championship in an Australian-developed Volvo 240 Turbo ('The Flying Brick'), and Jim Richards and Rickard Rydell famously won the 1998 AMP Bathurst 1000 in an S40 Super Tourer. Today, Volvo Car Australia is headquartered in Sydney and is leading the brand's global charge toward full electrification with the XC40/EX40, EX30, and XC90.",
        "models_catalog": [
            {
                "model_slug": "240-260",
                "name": "240 / 260 Series",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Family Car",
                "years_sold_au": {"start": 1974, "end": "1993"},
                "locally_built": True,
                "overview": "Indestructible Swedish family icon assembled locally in Melbourne and Brisbane, celebrated for world-class crashworthiness and 1986 ATCC victory.",
                "generations": [
                    {"series_code": "240-Series", "generation_name": "Volvo 240 / 260", "years": {"start": 1974, "end": 1993}, "body_styles": ["4-door sedan", "5-door wagon", "2-door coupe"], "summary": "B21/B23/B230 redblock four-cylinder and PRV B27/B28 V6; 242 GT, GL, GLE, and Group A Turbo."}
                ]
            },
            {
                "model_slug": "xc90",
                "name": "XC90",
                "vehicle_type": "SUV",
                "segment": "Large Luxury SUV",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "Landmark 7-seat luxury family SUV, establishing benchmark rollover safety and elegant Scandinavian luxury.",
                "generations": [
                    {"series_code": "P28", "generation_name": "XC90 First Generation", "years": {"start": 2003, "end": 2014}, "body_styles": ["5-door SUV"], "summary": "2.5T, D5 turbo diesel, 3.2 i6, and Yamaha-engineered 4.4L V8 (232kW)."},
                    {"series_code": "SPA", "generation_name": "XC90 Second Generation", "years": {"start": 2015, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "SPA modular platform, Thor's Hammer LED headlights, D5, T6, and T8 Recharge Twin Engine PHEV."}
                ]
            },
            {
                "model_slug": "xc60",
                "name": "XC60",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2009, "end": "Present"},
                "locally_built": False,
                "overview": "Volvo's global and Australian top-seller, introducing City Safety autonomous emergency braking to the Australian market.",
                "generations": [
                    {"series_code": "Y20-SPA", "generation_name": "XC60 1st & 2nd Gen", "years": {"start": 2009, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "First gen pioneered City Safety; second gen SPA platform brought B5 mild-hybrid and T8 PHEV."}
                ]
            }
        ]
    },
    "polestar": {
        "make_slug": "polestar",
        "name": "Polestar",
        "country_of_origin": "Sweden",
        "years_active_au": {"start": 2021, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Born from Volvo's touring car racing team and performance arm, Polestar launched Australia as an early pilot market before establishing an independent pure-electric luxury brand.",
        "australian_history": "Polestar has a special connection to Australia. In 2013, Australia was chosen as the sole global test market for the first factory-built Polestar road car: the Volvo S60 Polestar (50 limited-edition 257kW turbo inline-six sedans). Following its spin-off as a standalone electric performance brand jointly owned by Volvo and Geely, Polestar launched in Australia in late 2021 with the Polestar 2 liftback. Operating an online sales model with Polestar Spaces in Sydney, Melbourne, and Brisbane, the brand quickly established itself among Australia's leading premium EV sellers.",
        "models_catalog": [
            {
                "model_slug": "polestar-2",
                "name": "Polestar 2",
                "vehicle_type": "Liftback Sedan",
                "segment": "Medium Luxury EV",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Pure-electric performance fastback featuring Google Android Automotive OS and Öhlins dual-flow damping.",
                "generations": [
                    {"series_code": "P8", "generation_name": "Polestar 2", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-door liftback"], "summary": "Standard Range Single Motor, Long Range Single Motor (RWD facelift), and 350kW Long Range Dual Motor Performance Pack."}
                ]
            },
            {
                "model_slug": "polestar-3",
                "name": "Polestar 3",
                "vehicle_type": "SUV",
                "segment": "Large Luxury EV SUV",
                "years_sold_au": {"start": 2024, "end": "Present"},
                "locally_built": False,
                "overview": "Aerodynamic luxury electric SUV featuring dual-chamber air suspension and 380kW dual-motor AWD.",
                "generations": [
                    {"series_code": "P3", "generation_name": "Polestar 3", "years": {"start": 2024, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "111kWh battery, 610km range, torque-vectoring dual clutch, and SmartZone front sensor cluster."}
                ]
            }
        ]
    },
    "saab": {
        "make_slug": "saab",
        "name": "Saab",
        "country_of_origin": "Sweden",
        "years_active_au": {"start": 1962, "end": 2012},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Quirky, aerospace-inspired Swedish carmaker celebrated in Australia for turbocharging leadership, wraparound windscreens, and ignition keys between the front seats.",
        "australian_history": "Saab entered Australia in the early 1960s with the two-stroke 96 and V4. The brand gained a passionate following among Australian architects, academics, and doctors with the launch of the 99 Turbo in 1978 and the iconic 900. The classic Saab 900 Turbo and 900 Convertible became status symbols in Sydney and Melbourne through the 1980s. General Motors acquired a 50% stake in 1989 and full ownership in 2000, integrating Saab distribution into GM-Holden's network. Following GM's bankruptcy and Spyker's brief ownership, Saab ceased vehicle production globally in late 2011, and Saab Australia wound up operations in 2012.",
        "models_catalog": [
            {
                "model_slug": "900",
                "name": "900",
                "vehicle_type": "Hatchback / Sedan / Convertible",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1978, "end": 1998},
                "locally_built": False,
                "overview": "The definitive classic Saab, featuring aircraft cockpit ergonomics, front-hinged clamshell bonnet, and punchy turbo power.",
                "generations": [
                    {"series_code": "Classic-900", "generation_name": "Saab 900 Classic", "years": {"start": 1978, "end": 1993}, "body_styles": ["3-door hatch", "5-door hatch", "4-door sedan", "Convertible"], "summary": "Slant-four 2.0L B-engine and H-engine, Turbo, Turbo 16S, Aero, and iconic full four-seater Convertible."},
                    {"series_code": "NG900", "generation_name": "Saab 900 New Generation", "years": {"start": 1994, "end": 1998}, "body_styles": ["3-door hatch", "5-door hatch", "Convertible"], "summary": "GM2900 platform, Night Panel display, 2.0i, 2.3i, 2.5 V6, and 2.0 Turbo."}
                ]
            },
            {
                "model_slug": "9-3",
                "name": "9-3",
                "vehicle_type": "Sedan / SportCombi Wagon / Convertible",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1998, "end": 2011},
                "locally_built": False,
                "overview": "Successor to the 900, offered in Linear, Arc, Vector, Aero, and rare all-wheel drive Turbo X.",
                "generations": [
                    {"series_code": "YS3D-YS3F", "generation_name": "Saab 9-3 1st & 2nd Gen", "years": {"start": 1998, "end": 2011}, "body_styles": ["4-door sedan", "SportCombi wagon", "Convertible"], "summary": "First gen hatch/cabriolet; second gen Sport Sedan with ReAxs passive rear steering, 2.8T V6 Aero, and XWD."}
                ]
            }
        ]
    },
    "peugeot": {
        "make_slug": "peugeot",
        "name": "Peugeot",
        "country_of_origin": "France",
        "years_active_au": {"start": 1949, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Historic French marque immortalized in Australian outback rallying and local CKD assembly of 403, 404, 504, and 505 models at Heidelberg and Clayton, Victoria.",
        "australian_history": "Peugeot's legendary Australian reputation was forged in 1953 when Ken Tubman and John Marshall won the grueling 6,500-mile Redex Round Australia Reliability Trial in an unpretentious Peugeot 203, astounding the nation. Demand surged, leading to local assembly at Martin & King (Clayton) and later Renault's Heidelberg plant in Melbourne. The 403, 404, 504, and 505 were all assembled locally with high Australian content. The 504 won Wheels Car of the Year in 1969 and became famous for absorbing horrific Australian corrugations thanks to its long-travel independent suspension. Local assembly concluded in 1986. Distribution transitioned through Ateco, Sime Darby, and Inchcape. Modern Peugeot excels with the 208, 308, 2008, 3008, and 5008 SUVs.",
        "models_catalog": [
            {
                "model_slug": "504-505",
                "name": "504 / 505",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Family Car",
                "years_sold_au": {"start": 1969, "end": "1993"},
                "locally_built": True,
                "overview": "Locally assembled at Heidelberg and Clayton VIC, renowned for unmatched ride compliance, rally toughness, and Wheels Car of the Year honors.",
                "generations": [
                    {"series_code": "504", "generation_name": "Peugeot 504", "years": {"start": 1969, "end": 1983}, "body_styles": ["4-door sedan", "5-door wagon", "Ute"], "summary": "1.8L and 2.0L carburettor and mechanical Kugelfischer injection (TI), 2.3 Diesel, and rugged 7-seat Familiale."},
                    {"series_code": "505", "generation_name": "Peugeot 505", "years": {"start": 1980, "end": 1993}, "body_styles": ["4-door sedan", "5-door wagon"], "summary": "Assembled locally until 1986; GR, SR, STI, GTI (2.2L all-alloy OHC), Turbo Diesel, and GTi Turbo."}
                ]
            },
            {
                "model_slug": "206-208",
                "name": "206 / 207 / 208",
                "vehicle_type": "Hatchback / CC",
                "segment": "Light Car",
                "years_sold_au": {"start": 1999, "end": "Present"},
                "locally_built": False,
                "overview": "Peugeot's stylish city hatchbacks, including folding hardtop 206 CC and thrilling 208 GTi hot hatches.",
                "generations": [
                    {"series_code": "206-207", "generation_name": "Peugeot 206 & 207", "years": {"start": 1999, "end": 2012}, "body_styles": ["3-door hatch", "5-door hatch", "Coupe-Cabriolet CC", "Wagon"], "summary": "Wildly successful 206 XR, XT, GTi 138/180; followed by larger 207 with 1.6 VTi and GTi Turbo."},
                    {"series_code": "208", "generation_name": "Peugeot 208", "years": {"start": 2012, "end": "Present"}, "body_styles": ["3-door hatch", "5-door hatch"], "summary": "Introduced Peugeot i-Cockpit, 147kW-153kW 208 GTi, and second-gen pure-electric e-208."}
                ]
            },
            {
                "model_slug": "3008",
                "name": "3008",
                "vehicle_type": "SUV",
                "segment": "Medium SUV",
                "years_sold_au": {"start": 2010, "end": "Present"},
                "locally_built": False,
                "overview": "Distinctive European SUV that evolved from a crossover MPV into a sleek, avant-garde design award winner.",
                "generations": [
                    {"series_code": "T84-P84", "generation_name": "Peugeot 3008 1st & 2nd Gen", "years": {"start": 2010, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "First-gen split tailgate crossover; second-gen P84 European Car of the Year with i-Cockpit, Allure, GT, and GT Sport PHEV."}
                ]
            }
        ]
    },
    "renault": {
        "make_slug": "renault",
        "name": "Renault",
        "country_of_origin": "France",
        "years_active_au": {"start": 1950, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "French innovator that operated an extensive manufacturing plant at Heidelberg, Victoria from 1959 to 1981, and achieved modern acclaim through Renault Sport hot hatches and commercial vans.",
        "australian_history": "Renault has deep Australian manufacturing roots. In 1959, Renault took over assembly operations from Clyde Industries at Heidelberg, Victoria, establishing Renault Australia Pty Ltd in 1966. The Heidelberg plant built the Dauphine, R8, R10, R12, and R16, as well as contract-assembling Peugeot models. The Australian-built Renault 12 was uniquely evolved into the Australian-exclusive Renault Virage in 1978 with quad round headlights. In 1981, due to rationalization under the Button Car Plan, Renault sold the Heidelberg facility to LNC Industries. Modern Renault distribution returned via Ateco Automotive in 2021, driven by the Trafic and Master commercial vans, Koleos and Arkana SUVs, and celebrated Renault Sport models (Clio R.S. and Megane R.S.).",
        "models_catalog": [
            {
                "model_slug": "12-virage",
                "name": "12 / Virage",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Small / Medium Car",
                "years_sold_au": {"start": 1970, "end": "1980"},
                "locally_built": True,
                "overview": "Assembled at Heidelberg VIC; acclaimed for ride comfort and ruggedness, culminating in the unique Australian-styled Virage.",
                "generations": [
                    {"series_code": "R1170-Virage", "generation_name": "Renault 12 & Virage", "years": {"start": 1970, "end": 1980}, "body_styles": ["4-door sedan", "5-door wagon"], "summary": "1.3L and 1.4L engines; 1970 Wheels Car of the Year; updated to Australian quad-headlight Virage in 1978."}
                ]
            },
            {
                "model_slug": "megane",
                "name": "Megane",
                "vehicle_type": "Hatchback / Sedan / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1999, "end": "Present"},
                "locally_built": False,
                "overview": "French small car spanning distinctive bustle-back designs to legendary Nürburgring record-setting Megane R.S. hot hatches.",
                "generations": [
                    {"series_code": "Megane-II", "generation_name": "Megane II", "years": {"start": 2003, "end": 2009}, "body_styles": ["3-door hatch", "5-door hatch", "Sedan", "Coupe-Cabriolet CC"], "summary": "Famous 'shaking that ass' avant-garde styling, 2.0L Turbo Megane R.S. 225 and R26."},
                    {"series_code": "Megane-III-IV", "generation_name": "Megane III & IV", "years": {"start": 2010, "end": "Present"}, "body_styles": ["Coupe", "Hatch", "Wagon", "Sedan"], "summary": "Megane R.S. 250/265/275 Trophy; Megane IV with 4Control 4-wheel steering and 221kW Trophy."}
                ]
            },
            {
                "model_slug": "trafic",
                "name": "Trafic",
                "vehicle_type": "Van",
                "segment": "Medium Commercial Van",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "A stalwart of Australian trade and courier fleets, lauded for car-like cabin comfort, dCi diesel reliability, and long wheelbase options.",
                "generations": [
                    {"series_code": "X83-X82", "generation_name": "Trafic 2nd & 3rd Gen", "years": {"start": 2004, "end": "Present"}, "body_styles": ["Short-wheelbase van", "Long-wheelbase van", "Crew van"], "summary": "1.9 dCi and 2.0 dCi engines, progressing to twin-turbo 1.6 dCi and 2.0 dCi with EDC automatic."}
                ]
            }
        ]
    },
    "citroen": {
        "make_slug": "citroen",
        "name": "Citroën",
        "country_of_origin": "France",
        "years_active_au": {"start": 1923, "end": 2024},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "The avant-garde French innovator that gave Australia local assembly of the ID19/DS19, hydraulic magic-carpet ride comfort, and historic rally victories.",
        "australian_history": "Citroën had an extraordinary history in Australia spanning over a century. In 1925, an 11CV Citroën became the first car to drive completely around the perimeter of Australia (Nevill Westwood and Greg Davies). In the 1960s, Citroën cars—specifically the ID19 and DS19—were assembled locally in Heidelberg and Clayton, Victoria by Pressed Metal Corporation and Motor Producers Ltd. The hydropneumatic suspension proved peerless on rough Australian outback roads, leading a Citroën DS21 to outright victory in the 1970 Ampol Round Australia Trial. Imported by Ateco and later Inchcape, Citroën offered the CX, BX, Xantia, C5, and C4 Cactus. In August 2024, after 101 continuous years of sales, distributor Inchcape announced Citroën would withdraw from new car sales in Australia.",
        "models_catalog": [
            {
                "model_slug": "ds-id",
                "name": "DS / ID",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Large Executive Car",
                "years_sold_au": {"start": 1956, "end": "1975"},
                "locally_built": True,
                "overview": "The Goddess of automotive design, assembled in Victoria and celebrated for conquering the brutal Ampol Trial with hydropneumatic suspension.",
                "generations": [
                    {"series_code": "DS-Series", "generation_name": "Citroën DS & ID", "years": {"start": 1956, "end": 1975}, "body_styles": ["4-door sedan", "Safari wagon"], "summary": "Assembled in Melbourne in ID19 guise; directional swiveling headlamps on DS21/DS23, high-pressure hydraulics."}
                ]
            },
            {
                "model_slug": "c5-c5x",
                "name": "C5 / C5 X",
                "vehicle_type": "Sedan / Wagon / Crossover",
                "segment": "Medium / Large Car",
                "years_sold_au": {"start": 2001, "end": "2024"},
                "locally_built": False,
                "overview": "Flagship French cruiser featuring Hydractive III+ suspension and culminating in the innovative C5 X crossover fastback.",
                "generations": [
                    {"series_code": "X40-X7-E43", "generation_name": "C5 Generations", "years": {"start": 2001, "end": 2024}, "body_styles": ["Liftback", "Sedan", "Tourer wagon", "Crossover fastback"], "summary": "Hydractive III suspension; HDi twin-turbo diesels; ending with the high-riding C5 X 1.6 PureTech turbo."}
                ]
            }
        ]
    },
    "alpine": {
        "make_slug": "alpine",
        "name": "Alpine",
        "country_of_origin": "France",
        "years_active_au": {"start": 2018, "end": 2021},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Dieppe's legendary lightweight French sports car marque, selling the exquisite mid-engine A110 in Australia through bespoke Alpine centres.",
        "australian_history": "Renault officially launched the reborn Alpine brand in Australia in late 2018 with the mid-engined, aluminium-chassis A110 coupe. Operating dedicated Alpine showcases in Sydney and Melbourne, the brand was lauded by Australian motoring journalists for pure vehicle dynamics, featherweight 1,080kg kerb weight, and telepathic steering. Offered in Pure, Légende, and 215kW A110 S specifications, the car garnered critical acclaim. However, the introduction of strict ADR 85/00 side-impact pole crash test regulations in late 2021 forced Alpine to withdraw the A110 from Australia.",
        "models_catalog": [
            {
                "model_slug": "a110",
                "name": "A110",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2018, "end": "2021"},
                "locally_built": False,
                "overview": "Ultralight mid-engine aluminium two-seater sports car, powered by a 1.8-litre turbocharged four-cylinder with 7-speed Getrag wet dual-clutch.",
                "generations": [
                    {"series_code": "A110-Modern", "generation_name": "Alpine A110", "years": {"start": 2018, "end": 2021}, "body_styles": ["2-door coupe"], "summary": "Pure, Légende, Premiere Edition (185kW), and stiffer A110 S (215kW / 320Nm)."}
                ]
            }
        ]
    },
    "fiat": {
        "make_slug": "fiat",
        "name": "Fiat",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1901, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Italian automotive giant that assembled 500, 600, 1100, 1500, and 124 models in Sydney and Melbourne, and thrives today with the iconic modern 500 and Ducato van.",
        "australian_history": "Fiat has an extensive Australian footprint dating to the early 1900s. From 1957 through the 1970s, Fiat passenger cars—including the 500 'Bambino', 600, 1100, 1500, 124 sedan, and 125—were assembled locally under contract by Pressed Metal Corporation in Sydney and Motor Producers Ltd in Clayton, Melbourne. Fiats were praised for rev-happy twin-cam engines, 5-speed gearboxes, and four-wheel disc brakes. Distribution later moved through LNC Industries, Ateco Automotive, and Stellantis Australia. The retro 500 (Cinquecento) launched in 2008 and became a runaway urban success, alongside fiery Abarth 595/695 derivatives and the Ducato commercial van.",
        "models_catalog": [
            {
                "model_slug": "500-cinquecento",
                "name": "500 / Bambino",
                "vehicle_type": "Hatchback / Convertible",
                "segment": "City Car",
                "years_sold_au": {"start": 1957, "end": "Present"},
                "locally_built": True,
                "overview": "Beloved Italian design icon, assembled locally as the classic Bambino and reborn as the chic modern 500, Abarth, and electric 500e.",
                "generations": [
                    {"series_code": "Nuova-500", "generation_name": "Fiat Nuova 500 (Bambino)", "years": {"start": 1957, "end": 1975}, "body_styles": ["2-door saloon", "Convertible"], "summary": "Locally assembled air-cooled rear-engine 479cc-594cc twin; affectionately named the Bambino."},
                    {"series_code": "Typ 312", "generation_name": "Fiat 500 Modern", "years": {"start": 2008, "end": "Present"}, "body_styles": ["3-door hatch", "Cabriolet"], "summary": "1.2L, 1.4L 16V, TwinAir 2-cylinder turbo, Abarth 595/695 (up to 132kW), and 500e EV."}
                ]
            },
            {
                "model_slug": "ducato",
                "name": "Ducato",
                "vehicle_type": "Van / Cab-Chassis",
                "segment": "Large Commercial Van / Motorhome",
                "years_sold_au": {"start": 2002, "end": "Present"},
                "locally_built": False,
                "overview": "The dominant base vehicle for the Australian motorhome and RV industry, featuring front-wheel drive and torquey MultiJet turbo-diesels.",
                "generations": [
                    {"series_code": "Typ 244-250", "generation_name": "Ducato Generations", "years": {"start": 2002, "end": "Present"}, "body_styles": ["Medium/Long/Extra-long van", "Cab-chassis"], "summary": "2.3L and 3.0L MultiJet turbo diesels with 9-speed torque-converter automatic."}
                ]
            }
        ]
    },
    "alfa-romeo": {
        "make_slug": "alfa-romeo",
        "name": "Alfa Romeo",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1960, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The passionate Italian driver's marque, renowned in Australia for melodic twin-cam engines, Bathurst class victories, and the Giorgio-platform Giulia and Stelvio.",
        "australian_history": "Alfa Romeo established strong Australian presence in the 1960s with distributor Alec Mildren, whose racing team campaigned Giulia and GTA models with immense success. At the Bathurst 500, Alfa Romeo GT and 1750 GTVs won their classes repeatedly. The 105 Series Giulia, Bertone Coupe (1750/2000 GTV), and Spider Veloce became Australian motoring royalty. Transaxle models like the Alfetta, GTV6, and 75 followed in the 1970s and 1980s. Modern Alfa Romeo is represented by the 156, 147, 159, and the celebrated rear-wheel-drive Giorgio platform: the Giulia sports sedan and Stelvio SUV, crowned by 375kW Ferrari-developed 2.9L twin-turbo V6 Quadrifoglio models.",
        "models_catalog": [
            {
                "model_slug": "giulia",
                "name": "Giulia",
                "vehicle_type": "Sedan",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1963, "end": "Present"},
                "locally_built": False,
                "overview": "The quintessential sports sedan across classic 105 series and modern Giorgio-platform Type 952 with 50:50 weight balance.",
                "generations": [
                    {"series_code": "105-Series", "generation_name": "Giulia 105 Series", "years": {"start": 1963, "end": 1977}, "body_styles": ["4-door sedan"], "summary": "Giulia TI, Super, and Nuova Super with all-alloy DOHC twin-cam 1.3L and 1.6L and 5-speed manual."},
                    {"series_code": "Type 952", "generation_name": "Giulia Modern", "years": {"start": 2017, "end": "Present"}, "body_styles": ["4-door sedan"], "summary": "Carbon-fibre driveshaft, 2.0L Turbo (147kW/206kW Veloce), and 375kW 2.9L Twin-Turbo V6 Quadrifoglio."}
                ]
            },
            {
                "model_slug": "105-gtv-spider",
                "name": "105 GTV / Spider",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1965, "end": "1994"},
                "locally_built": False,
                "overview": "Bertone-designed Giulia Sprint GT, 1750 GTV, and Pininfarina Spider; revered collector cars in Australia.",
                "generations": [
                    {"series_code": "105-Coupe", "generation_name": "GTV Stepnose, 1750 & 2000", "years": {"start": 1965, "end": 1976}, "body_styles": ["2-door coupe"], "summary": "Sprint GT, GT Veloce, 1750 GTV, and 2000 GTV with limited-slip differential and 4-wheel disc brakes."},
                    {"series_code": "105-115-Spider", "generation_name": "Spider Duetto & Series 2-4", "years": {"start": 1967, "end": 1994}, "body_styles": ["2-door convertible"], "summary": "Osso di seppia 'boat tail' Duetto through Kamm-tail Spider 2000 Veloce."}
                ]
            },
            {
                "model_slug": "stelvio",
                "name": "Stelvio",
                "vehicle_type": "SUV",
                "segment": "Medium Luxury SUV",
                "years_sold_au": {"start": 2018, "end": "Present"},
                "locally_built": False,
                "overview": "Alfa Romeo's first production SUV, sharing the Giorgio architecture and steering sharpness of the Giulia.",
                "generations": [
                    {"series_code": "Type 949", "generation_name": "Stelvio", "years": {"start": 2018, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Q4 all-wheel drive, 2.0T (147kW/206kW Veloce), and 375kW Quadrifoglio with torque-vectoring rear diff."}
                ]
            }
        ]
    },
    "ferrari": {
        "make_slug": "ferrari",
        "name": "Ferrari",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1952, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The pinnacle of Prancing Horse exotica in Australia, with privateer motorsport heritage dating to the early 1950s and direct factory subsidiary Ferrari Australasia established in 2013.",
        "australian_history": "Scuderia Veloce founder David McKay imported Australia's first racing Ferraris in the 1950s, driving a 250 GT to victory at Bathurst in 1960. W.H. Lowe and Maranello Concessionaires (Ateco) distributed road cars before Ferrari Australasia assumed factory control in 2013. Australian collectors prize models from the 246 Dino, 308 GTB, Testarossa, and F40 through to mid-engine V8 icons (F355, 360, 458 Italia) and modern hybrid hypercars (SF90, 296 GTB, and Purosangue V12).",
        "models_catalog": [
            {
                "model_slug": "308-328",
                "name": "308 / 328",
                "vehicle_type": "Coupe / Targa",
                "segment": "Supercar",
                "years_sold_au": {"start": 1976, "end": "1989"},
                "locally_built": False,
                "overview": "Pininfarina-styled mid-engine V8 icons, popularised by television and heralded for dry-sump 2.9L and 3.2L engines.",
                "generations": [
                    {"series_code": "F106", "generation_name": "Ferrari 308 & 328", "years": {"start": 1976, "end": 1989}, "body_styles": ["Coupe GTB", "Targa GTS"], "summary": "Carburettor, 2-valve injection, Quattrovalvole 4-valve, and refined 328 GTB/GTS."}
                ]
            },
            {
                "model_slug": "458-italia",
                "name": "458 Italia",
                "vehicle_type": "Coupe / Spider",
                "segment": "Supercar",
                "years_sold_au": {"start": 2010, "end": "2015"},
                "locally_built": False,
                "overview": "Ferrari's final naturally aspirated mid-engine V8, screaming to a 9,000rpm redline and producing 419kW (570hp).",
                "generations": [
                    {"series_code": "F142", "generation_name": "Ferrari 458", "years": {"start": 2010, "end": 2015}, "body_styles": ["Coupe", "Spider", "Speciale"], "summary": "4.5L flat-plane V8, 7-speed dual-clutch, E-Diff, and 445kW Speciale with active aerodynamics."}
                ]
            }
        ]
    },
    "lamborghini": {
        "make_slug": "lamborghini",
        "name": "Lamborghini",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1965, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Sant'Agata's raging bull supercars in Australia, captivating enthusiasts from the Miura and Countach through the V10 Gallardo and Huracán, and Urus super-SUV.",
        "australian_history": "Lamborghini entered Australia through specialist agents in the 1960s with the 350GT and Miura. In the 1980s, the scissor-doored Countach captured bedroom posters across the nation. Under Audi/Volkswagen Group ownership, Lamborghini built factory-backed retail networks in Sydney, Melbourne, Brisbane, and Perth. The V10 Gallardo (over 14,000 produced globally) and Huracán democratized everyday supercar usability, while the Urus super-SUV propelled the marque to historic Australian sales records.",
        "models_catalog": [
            {
                "model_slug": "gallardo-huracan",
                "name": "Gallardo / Huracán",
                "vehicle_type": "Coupe / Spyder",
                "segment": "Supercar",
                "years_sold_au": {"start": 2004, "end": "2024"},
                "locally_built": False,
                "overview": "Naturally aspirated V10 mid-engine supercars, offering spine-tingling sound, all-wheel drive, and rear-wheel-drive dynamics.",
                "generations": [
                    {"series_code": "L140", "generation_name": "Gallardo", "years": {"start": 2004, "end": 2014}, "body_styles": ["Coupe", "Spyder"], "summary": "5.0L and 5.2L V10, gated 6-speed manual and e-gear, LP560-4, and lightweight Superleggera."},
                    {"series_code": "LB724", "generation_name": "Huracán", "years": {"start": 2014, "end": 2024}, "body_styles": ["Coupe", "Spyder"], "summary": "5.2L V10 (up to 470kW), 7-speed dual clutch, LP610-4, Performante with ALA aero, EVO, STO, and off-road Sterrato."}
                ]
            },
            {
                "model_slug": "urus",
                "name": "Urus",
                "vehicle_type": "Super SUV",
                "segment": "Luxury Performance SUV",
                "years_sold_au": {"start": 2018, "end": "Present"},
                "locally_built": False,
                "overview": "The world's first Super Sport Utility Vehicle, powered by a 4.0-litre twin-turbo V8 producing up to 490kW.",
                "generations": [
                    {"series_code": "Urus-Modern", "generation_name": "Lamborghini Urus", "years": {"start": 2018, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Twin-turbo 4.0L V8, carbon-ceramic brakes, Urus S, and track-honed Urus Performante."}
                ]
            }
        ]
    },
    "maserati": {
        "make_slug": "maserati",
        "name": "Maserati",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1956, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The Trident marque of Modena, celebrated in Australia for grand touring elegance, Ferrari-built V8 symphonies, and bespoke Italian luxury.",
        "australian_history": "Maserati's Australian racing lore began when Stan Jones won the 1959 Australian Grand Prix at Longford in a Maserati 250F. Road car imports included the 3500 GT, Ghibli, Merak, and Biturbo series. Ateco Automotive distributed Maserati in Australia from 2001 to 2023, expanding the brand with the Pininfarina-designed GranTurismo, Quattroporte, Ghibli sports sedan, and Levante SUV. In 2023, Maserati assumed direct factory distribution across Australia and New Zealand.",
        "models_catalog": [
            {
                "model_slug": "granturismo",
                "name": "GranTurismo",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Grand Tourer",
                "years_sold_au": {"start": 2008, "end": "Present"},
                "locally_built": False,
                "overview": "Pininfarina-styled 2+2 grand tourer celebrated for one of the most magnificent exhaust notes in motoring history.",
                "generations": [
                    {"series_code": "M145", "generation_name": "GranTurismo First Generation", "years": {"start": 2008, "end": 2019}, "body_styles": ["Coupe", "GranCabrio convertible"], "summary": "Ferrari-built naturally aspirated 4.2L and 4.7L crossplane V8 (up to 338kW in MC Stradale)."},
                    {"series_code": "M189", "generation_name": "GranTurismo Second Generation", "years": {"start": 2023, "end": "Present"}, "body_styles": ["Coupe", "GranCabrio"], "summary": "Twin-turbo 3.0L Nettuno V6 (Modena, Trofeo) and all-electric 800V tri-motor Folgore."}
                ]
            }
        ]
    },
    "lancia": {
        "make_slug": "lancia",
        "name": "Lancia",
        "country_of_origin": "Italy",
        "years_active_au": {"start": 1960, "end": 1988},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Pioneering Italian engineering marque beloved by Australian enthusiasts for the Fulvia, Flavia, Beta, and rally-legend Delta Integrale.",
        "australian_history": "Lancia was imported into Australia in the 1960s and 1970s by Grenville Motors and independent distributors, attracting discerning drivers with front-wheel drive engineering, narrow-angle V4 engines (Fulvia), and boxer-fours (Flavia). The Lancia Beta range—including Coupe, HPE, and mid-engine Montecarlo—was sold in Australia through the 1970s and 1980s. While official factory imports ceased in the late 1980s, Australian rally and Italian car enthusiasts privately imported dozens of Group A World Rally Championship homologation heroes, notably the Lancia Delta HF Integrale and Integrale Evoluzione.",
        "models_catalog": [
            {
                "model_slug": "beta",
                "name": "Beta",
                "vehicle_type": "Sedan / Coupe / HPE / Spider",
                "segment": "Medium Sports Car",
                "years_sold_au": {"start": 1974, "end": "1985"},
                "locally_built": False,
                "overview": "Fiat twin-cam powered sports range featuring transverse front-wheel drive and MacPherson strut suspension.",
                "generations": [
                    {"series_code": "Beta-Series", "generation_name": "Lancia Beta", "years": {"start": 1974, "end": 1985}, "body_styles": ["Berlina sedan", "Coupe", "HPE shooting brake", "Spider targa"], "summary": "Lampredi twin-cam 1.6L, 1.8L, and 2.0L Volumex supercharged engines."}
                ]
            },
            {
                "model_slug": "delta-integrale",
                "name": "Delta HF Integrale",
                "vehicle_type": "Hatchback",
                "segment": "Rally Homologation Sports Car",
                "years_sold_au": {"start": 1987, "end": "1994"},
                "locally_built": False,
                "overview": "Six-time consecutive WRC champion rally icon, revered in Australia with private imports and collector status.",
                "generations": [
                    {"series_code": "Delta-HF", "generation_name": "Delta HF 4WD & Integrale", "years": {"start": 1987, "end": 1994}, "body_styles": ["5-door hatchback"], "summary": "2.0L Turbo 8V/16V, permanent Ferguson 4WD with Torsen rear differential, Evo 1, and Evo 2 (158kW)."}
                ]
            }
        ]
    }
}
