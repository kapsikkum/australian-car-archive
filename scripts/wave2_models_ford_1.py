"""
Wave 2 Deep-Dive Model Data: Ford Classics and Compacts (Part 1)
Models:
13. Cortina
14. Escort
15. Capri
16. Laser
"""
from typing import Any, Dict

MODEL_CORTINA: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "cortina",
    "name": "Ford Cortina",
    "vehicle_type": "Sedan / Station Wagon",
    "segment": "Compact / Mid-size",
    "years_sold_au": {"start": 1962, "end": 1982},
    "locally_built": True,
    "assembly_plants_au": [
        "Broadmeadows, Victoria",
        "Homebush, New South Wales",
        "Geelong, Victoria (engines and stampings)"
    ],
    "overview": "The Ford Cortina held a distinguished two-decade tenure in Australia, evolving from a nimble British compact into a uniquely Australian six-cylinder muscle sedan. Assembled locally from 1962 (Mk1 and Mk2), the Cortina achieved legendary status when the Bob Jane / Harry Firth Cortina GT500 won the 1965 Armstrong 500 at Mount Panorama, Bathurst. In 1971, Ford Australia undertook a daring local engineering feat with the TC and TD Cortina: modifying the British 'Coke-bottle' body with an elongated front structure to accommodate Ford Australia's heavy 200ci (3.3L) and 250ci (4.1L) Falcon inline-six engines. The European-styled TE (1977) and TF (1980) brought crisp lines, Ghia luxury, and the sporty X-Pack before being succeeded by the Mazda-based Telstar in 1982.",
    "australian_market_notes": "The 6-cylinder Cortina TC/TD was a uniquely Australian phenomenon. Packing the Falcon's big 250ci (4.1L) engine into a lightweight 1,100 kg body gave it exceptional straight-line acceleration, running 0-100 km/h in 8.5 seconds—faster than many contemporary V8s. Local engineers developed heavier front springs, upgraded disc brakes, and reinforced front crossmembers to handle Australian conditions.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Mk1-Mk2",
            "generation_name": "Mk1 & Mk2 Cortina",
            "years": {"start": 1962, "end": 1971},
            "body_styles": ["2-door sedan", "4-door sedan", "5-door wagon"],
            "platform": "Ford UK Cortina unibody",
            "ancap_rating": None,
            "summary": "Australian assembly at Broadmeadows and Homebush. Won 1965 Bathurst 500 with the homologated Cortina GT500, featuring twin fuel tanks and Weber carburation.",
            "engines": [
                {
                    "engine_code": "Kent-1500-GT500",
                    "name": "Ford 1.5L High-Performance OHV Inline-4",
                    "displacement_cc": 1498,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 68.0,
                    "power_rpm": "6000",
                    "torque_nm": 132.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Twin-choke Weber carburettor, competition camshaft; homologated for Bathurst."
                },
                {
                    "engine_code": "Kent-1600-Crossflow",
                    "name": "Ford Kent 1.6L Crossflow OHV Inline-4",
                    "displacement_cc": 1599,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 56.0,
                    "power_rpm": "5300",
                    "torque_nm": 125.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Crossflow cylinder head introduced on Mk2 in 1968."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cortina GT",
                    "years": {"start": 1963, "end": 1971},
                    "body_styles": ["2-door sedan", "4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor"],
                    "msrp_aud_min": 2190,
                    "msrp_aud_max": 2490,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 880,
                    "standard_features": ["GT sports instrumentation with tachometer", "Front bucket seats", "Front disc brakes", "Lowered sports suspension"],
                    "notes": "Armstrong 500 race winner."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cortina GT",
                    "body_style": "2-door sedan",
                    "engine_code": "Kent-1500-GT500",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 2250,
                    "power_kw": 68.0,
                    "torque_nm": 132.0,
                    "fuel_l_100km": 9.2,
                    "towing_braked_kg": 750,
                    "notes": "1965 Bathurst 500 winner specification."
                }
            ]
        },
        {
            "series_code": "TC-TD",
            "generation_name": "TC / TD Cortina (6-Cylinder)",
            "years": {"start": 1971, "end": 1977},
            "body_styles": ["2-door sedan", "4-door sedan", "5-door wagon"],
            "platform": "Ford TC platform (Australian lengthened)",
            "ancap_rating": None,
            "summary": "Australian-engineered 'Big Six' Cortina. Front chassis extended to swallow Ford Australia's 200ci (3.3L) and 250ci (4.1L) Falcon straight-six engines.",
            "engines": [
                {
                    "engine_code": "Falcon-200-I6",
                    "name": "Ford Falcon 200ci (3.3L) OHV Inline-6",
                    "displacement_cc": 3277,
                    "displacement_litres": 3.3,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 86.0,
                    "power_rpm": "4400",
                    "torque_nm": 258.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Australian Falcon six-cylinder powerplant."
                },
                {
                    "engine_code": "Falcon-250-I6",
                    "name": "Ford Falcon 250ci (4.1L) OHV Inline-6",
                    "displacement_cc": 4089,
                    "displacement_litres": 4.1,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 116.0,
                    "power_rpm": "4400",
                    "torque_nm": 325.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Big 4.1-litre Falcon six; gave Cortina devastating acceleration."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cortina XLE 250",
                    "years": {"start": 1973, "end": 1977},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed automatic Borg-Warner 35", "4-speed manual floor"],
                    "msrp_aud_min": 3790,
                    "msrp_aud_max": 4290,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1145,
                    "standard_features": [
                        "250ci 4.1L Falcon inline-six standard",
                        "Vinyl roof and full side bodyside moldings",
                        "Woodgrain dash and sports console",
                        "Cloth/vinyl bucket seats and sports steering wheel",
                        "Power front disc brakes and sports road wheels"
                    ],
                    "notes": "Australian luxury muscle sleeper."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cortina XLE 250",
                    "body_style": "Sedan",
                    "engine_code": "Falcon-250-I6",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 3890,
                    "power_kw": 116.0,
                    "torque_nm": 325.0,
                    "fuel_l_100km": 12.8,
                    "towing_braked_kg": 1200,
                    "notes": "4.1L 6-cylinder pocket muscle car."
                }
            ]
        },
        {
            "series_code": "TE-TF",
            "generation_name": "TE / TF Cortina",
            "years": {"start": 1977, "end": 1982},
            "body_styles": ["4-door sedan", "5-door wagon"],
            "platform": "Ford Taunus / Cortina Mk IV/V",
            "ancap_rating": None,
            "summary": "Crisp European styling fitted with Australian Crossflow 3.3L and 4.1L sixes alongside 2.0L Pinto four. Ghia luxury appointments and X-Pack sports option.",
            "engines": [
                {
                    "engine_code": "Crossflow-4.1-I6",
                    "name": "Ford Crossflow 4.1L (250ci) Inline-6",
                    "displacement_cc": 4089,
                    "displacement_litres": 4.1,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 98.0,
                    "power_rpm": "4000",
                    "torque_nm": 298.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Aluminium cylinder head Crossflow six (from 1980)."
                }
            ],
            "badges": [
                {
                    "badge_name": "Cortina Ghia",
                    "years": {"start": 1977, "end": 1982},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed automatic", "4-speed manual"],
                    "msrp_aud_min": 6890,
                    "msrp_aud_max": 8290,
                    "fuel_consumption_l_100km": 12.4,
                    "kerb_weight_kg": 1210,
                    "standard_features": [
                        "4.1L Crossflow engine standard",
                        "Velour seats and cut-pile carpet",
                        "Tinted glass and digital clock",
                        "Cast alloy wheels",
                        "Power steering and intermittent wipers"
                    ],
                    "notes": "Top-tier luxury specification."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Cortina Ghia",
                    "body_style": "Sedan",
                    "engine_code": "Crossflow-4.1-I6",
                    "transmission": "3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 7490,
                    "power_kw": 98.0,
                    "torque_nm": 298.0,
                    "fuel_l_100km": 12.4,
                    "towing_braked_kg": 1200,
                    "notes": "4.1L Crossflow automatic Ghia saloon."
                }
            ]
        }
    ]
}

MODEL_ESCORT: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "escort",
    "name": "Ford Escort",
    "vehicle_type": "2-door Coupe / 4-door Sedan / 2-door Panel Van",
    "segment": "Small / Compact",
    "years_sold_au": {"start": 1970, "end": 1981},
    "locally_built": True,
    "assembly_plants_au": [
        "Homebush, New South Wales"
    ],
    "overview": "The Ford Escort was Ford Australia's frontline small car and grassroots rally champion throughout the 1970s. Manufactured at Ford's Homebush plant in Sydney, the Australian Mk1 (1970-1975) featured the classic 'dogbone' front grille, Kent Crossflow engines (1.1L, 1.3L, and 1.6L GT), and the legendary imported Twin Cam and RS1600. In 1975, the Australian Mk2 debuted with a squarer aerodynamic profile. Ford Australia equipped the Mk2 with the lively 1.6L Kent and the potent 2.0L OHC Pinto engine, culminating in the iconic Escort RS2000 featuring a polyurethane droop-snoot front nose, four-spoke alloy wheels, Scheel sports bucket seats, and rally-bred handling.",
    "australian_market_notes": "Australian Escorts featured unique local content including Australian-made glass, batteries, interior trim, and heavy-duty front suspension struts tailored to corrugated rural backroads. The Escort RS2000 was an instant youth idol, while the Escort Sundowner panel van tapped into the 1970s surf van craze with bold bodyside sunset decals and rear bubble port-hole windows.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Mk1",
            "generation_name": "Mk1 Escort",
            "years": {"start": 1970, "end": 1975},
            "body_styles": ["2-door coupe", "4-door sedan", "2-door panel van"],
            "platform": "Ford Escort Mk1 unibody",
            "ancap_rating": None,
            "summary": "Homebush, NSW manufacturing. Dogbone grille, round headlights, Kent Crossflow engines, and the rare Twin Cam homologation specials.",
            "engines": [
                {
                    "engine_code": "Kent-1.3L",
                    "name": "Ford Kent 1.3L Crossflow OHV Inline-4",
                    "displacement_cc": 1298,
                    "displacement_litres": 1.3,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 43.0,
                    "power_rpm": "5300",
                    "torque_nm": 95.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Mainstream high-economy four-cylinder."
                },
                {
                    "engine_code": "Kent-1.6L-GT",
                    "name": "Ford Kent 1.6L GT Crossflow OHV Inline-4",
                    "displacement_cc": 1599,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 64.0,
                    "power_rpm": "5400",
                    "torque_nm": 125.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Twin-choke Weber carburettor, extractors; powers Escort GT 1600."
                }
            ],
            "badges": [
                {
                    "badge_name": "Escort 1600 GT",
                    "years": {"start": 1970, "end": 1975},
                    "body_styles": ["2-door coupe", "4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor"],
                    "msrp_aud_min": 2490,
                    "msrp_aud_max": 2790,
                    "fuel_consumption_l_100km": 8.8,
                    "kerb_weight_kg": 875,
                    "standard_features": ["GT sports instrumentation", "Front disc brakes", "Radial ply tyres", "High-back bucket seats"],
                    "notes": "Rally-bred sports sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Escort 1600 GT",
                    "body_style": "2-door coupe",
                    "engine_code": "Kent-1.6L-GT",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 2550,
                    "power_kw": 64.0,
                    "torque_nm": 125.0,
                    "fuel_l_100km": 8.8,
                    "towing_braked_kg": 750,
                    "notes": "Classic Mk1 sports coupe."
                }
            ]
        },
        {
            "series_code": "Mk2",
            "generation_name": "Mk2 Escort",
            "years": {"start": 1975, "end": 1981},
            "body_styles": ["2-door coupe", "4-door sedan", "2-door panel van"],
            "platform": "Ford Escort Mk2 unibody",
            "ancap_rating": None,
            "summary": "Squared aerodynamic body, 2.0L Pinto OHC engine, Sundowner lifestyle panel van, and the iconic Australian Escort RS2000 with polyurethane droop-snoot nose.",
            "engines": [
                {
                    "engine_code": "Pinto-2.0L",
                    "name": "Ford Pinto 2.0L OHC Inline-4",
                    "displacement_cc": 1993,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 70.0,
                    "power_rpm": "5200",
                    "torque_nm": 152.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Twin-choke Weber carburettor; standard on RS2000 and optional on GL/Ghia."
                }
            ],
            "badges": [
                {
                    "badge_name": "RS2000",
                    "years": {"start": 1976, "end": 1980},
                    "body_styles": ["2-door coupe", "4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor"],
                    "msrp_aud_min": 5190,
                    "msrp_aud_max": 6290,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 950,
                    "standard_features": [
                        "2.0L OHC Pinto engine with twin-choke Weber",
                        "Polyurethane aerodynamic droop-snoot front nose with quad headlights",
                        "Four-spoke alloy sports wheels",
                        "Scheel high-bolstered sports bucket seats",
                        "Lowered heavy-duty sports suspension and front disc brakes"
                    ],
                    "notes": "Legendary Australian touring car and rally hotrod."
                },
                {
                    "badge_name": "Sundowner Van",
                    "years": {"start": 1977, "end": 1980},
                    "body_styles": ["Panel Van"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor"],
                    "msrp_aud_min": 4490,
                    "msrp_aud_max": 5150,
                    "fuel_consumption_l_100km": 9.8,
                    "kerb_weight_kg": 980,
                    "standard_features": [
                        "Rear side bubble port-hole windows",
                        "Sunset bodyside stripe graphics",
                        "Carpeted rear cargo area",
                        "Sports road wheels"
                    ],
                    "notes": "Lifestyle surf panel van competitor to Holden Sandman."
                }
            ],
            "configurations": [
                {
                    "badge_name": "RS2000",
                    "body_style": "2-door coupe",
                    "engine_code": "Pinto-2.0L",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 5490,
                    "power_kw": 70.0,
                    "torque_nm": 152.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 900,
                    "notes": "Definitive droop-snoot Aussie RS2000 coupe."
                }
            ]
        }
    ]
}

MODEL_CAPRI: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "capri",
    "name": "Ford Capri",
    "vehicle_type": "2-door Sports Coupe / 2-door Roadster/Convertible (2+2)",
    "segment": "Sports Car",
    "years_sold_au": {"start": 1969, "end": 1994},
    "locally_built": True,
    "assembly_plants_au": [
        "Homebush, New South Wales (Mk1 coupe, 1969-1972)",
        "Broadmeadows / Campbellfield, Victoria (SA-SE convertible, 1989-1994)"
    ],
    "overview": "The Ford Capri represents two bold chapters of Australian automotive innovation. In May 1969, Ford Australia began assembling the sleek Mk1 Capri sports coupe at Homebush, NSW, offering the 1600cc Kent and the potent 3.0-litre 'Essex' V6 in the revered Capri GT 3000 (101 kW / 136 bhp), instantly creating an Australian street and track favorite. In 1989, Ford Australia embarked on Project SA30: designing and manufacturing a dedicated front-wheel-drive 2+2 roadster convertible in Campbellfield, Victoria. Styled by Ghia in Turin and utilizing Mazda 323 mechanicals, the Australian-built Capri (SA, SB, SC, SE) was exported in huge numbers to North America as the Mercury Capri. It produced the blistering turbocharged Capri XR2 and the rare Australian Tickford-tuned Capri Clubsprint Turbo.",
    "australian_market_notes": "The Australian-built SA-SE convertible was a landmark manufacturing achievement for Ford Australia, generating vital export income ($1 billion+) with over 66,000 built. The limited-production Capri Clubsprint by Tickford Vehicle Engineering (TVE) featured aggressive front air dams, high-flow turbocharger boosting to 105 kW, Momo steering wheel, and bespoke Australian-tuned sports suspension.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Mk1",
            "generation_name": "Mk1 Capri Coupe",
            "years": {"start": 1969, "end": 1972},
            "body_styles": ["2-door fastback coupe"],
            "platform": "Ford Capri unibody",
            "ancap_rating": None,
            "summary": "Assembled at Homebush, NSW. Fastback muscle styling, 1600 GT four-cylinder and the thunderous 3.0L Essex V6 GT 3000.",
            "engines": [
                {
                    "engine_code": "Essex-3.0-V6",
                    "name": "Ford Essex 3.0L OHV V6",
                    "displacement_cc": 2994,
                    "displacement_litres": 3.0,
                    "cylinders": 6,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 101.0,
                    "power_rpm": "5000",
                    "torque_nm": 247.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.9:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Twin-choke Weber 38-DGAS carburettor, cast iron 60-degree V6; 136 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "GT 3000 (V6)",
                    "years": {"start": 1970, "end": 1972},
                    "body_styles": ["Coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "3-speed Borg-Warner automatic"],
                    "msrp_aud_min": 3290,
                    "msrp_aud_max": 3650,
                    "fuel_consumption_l_100km": 12.2,
                    "kerb_weight_kg": 1060,
                    "standard_features": [
                        "3.0L Essex V6 engine",
                        "Matte black bonnet with dual pins",
                        "Rostyle sports steel wheels",
                        "Twin sports exhausts",
                        "Full sports instrumentation with tachometer and oil pressure"
                    ],
                    "notes": "Classic Australian V6 muscle coupe."
                }
            ],
            "configurations": [
                {
                    "badge_name": "GT 3000 (V6)",
                    "body_style": "Coupe",
                    "engine_code": "Essex-3.0-V6",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 3290,
                    "power_kw": 101.0,
                    "torque_nm": 247.0,
                    "fuel_l_100km": 12.2,
                    "towing_braked_kg": 900,
                    "notes": "101 kW V6 4-speed manual fastback."
                }
            ]
        },
        {
            "series_code": "SA-SE-Convertible",
            "generation_name": "SA / SB / SC / SE Capri Convertible",
            "years": {"start": 1989, "end": 1994},
            "body_styles": ["2-door convertible (2+2)"],
            "platform": "Ford SA30 platform (Mazda 323 derivative)",
            "ancap_rating": None,
            "summary": "Australian-designed and manufactured front-wheel-drive 2+2 convertible in Campbellfield, Victoria. Exported globally. Searing 1.6L Turbo XR2 and TVE Clubsprint.",
            "engines": [
                {
                    "engine_code": "Mazda-B6-1.6L",
                    "name": "Ford / Mazda B6 1.6L DOHC 16V Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 77.0,
                    "power_rpm": "6000",
                    "torque_nm": 137.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Multi-point electronic fuel injection."
                },
                {
                    "engine_code": "Mazda-B6T-1.6L-Turbo",
                    "name": "Ford / Mazda B6T 1.6L DOHC 16V Turbo Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 100.0,
                    "power_rpm": "5500",
                    "torque_nm": 184.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "7.9:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "IHI RHB5 water-cooled turbocharger with air-to-air intercooler. Upgraded to 105 kW in Clubsprint."
                }
            ],
            "badges": [
                {
                    "badge_name": "XR2 Turbo",
                    "years": {"start": 1989, "end": 1994},
                    "body_styles": ["Convertible"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 25990,
                    "msrp_aud_max": 29990,
                    "fuel_consumption_l_100km": 7.9,
                    "kerb_weight_kg": 1055,
                    "standard_features": [
                        "100 kW 1.6L Turbo engine",
                        "14-inch sports alloy wheels",
                        "Rear boot lid spoiler",
                        "Power windows and mirrors",
                        "Folding manual canvas soft-top with optional hardtop"
                    ],
                    "notes": "Australian-manufactured turbo convertible."
                },
                {
                    "badge_name": "Clubsprint Turbo",
                    "years": {"start": 1992, "end": 1994},
                    "body_styles": ["Convertible"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 34990,
                    "msrp_aud_max": 37990,
                    "fuel_consumption_l_100km": 8.2,
                    "kerb_weight_kg": 1080,
                    "standard_features": [
                        "Tickford Vehicle Engineering (TVE) performance package",
                        "105 kW upgraded turbo calibration",
                        "Quad round headlamp nose cone and unique round tail lights",
                        "16-inch TVE alloy wheels and Michelin tyres",
                        "Momo leather steering wheel and gear knob"
                    ],
                    "notes": "Rare collector model; built by Tickford in Campbellfield."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XR2 Turbo",
                    "body_style": "Convertible",
                    "engine_code": "Mazda-B6T-1.6L-Turbo",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 25990,
                    "power_kw": 100.0,
                    "torque_nm": 184.0,
                    "fuel_l_100km": 7.9,
                    "towing_braked_kg": 750,
                    "notes": "Australian-built 1.6L Turbo convertible."
                },
                {
                    "badge_name": "Clubsprint Turbo",
                    "body_style": "Convertible",
                    "engine_code": "Mazda-B6T-1.6L-Turbo",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 34990,
                    "power_kw": 105.0,
                    "torque_nm": 190.0,
                    "fuel_l_100km": 8.2,
                    "towing_braked_kg": 750,
                    "notes": "Tickford-tuned Australian convertible."
                }
            ]
        }
    ]
}

MODEL_LASER: Dict[str, Any] = {
    "make_slug": "ford",
    "model_slug": "laser",
    "name": "Ford Laser",
    "vehicle_type": "3-door & 5-door Hatchback / 4-door Sedan / 5-door Wagon",
    "segment": "Small",
    "years_sold_au": {"start": 1981, "end": 2002},
    "locally_built": True,
    "assembly_plants_au": [
        "Homebush, New South Wales (KA, KB, KC, KE, KF, KH, 1981-1994)",
        "Hofu, Japan (KJ, KL, KQ, 1994-2002)"
    ],
    "overview": "The Ford Laser was one of Australia's most beloved small cars, dominating private sales and motoring awards across the 1980s and 1990s. Born from Ford's global partnership with Mazda (sharing the 323 platform), the Laser was manufactured at Ford's Homebush assembly plant in Sydney with distinct styling penned by Ford Australia's design studio. The Laser spawned the iconic 'TX3' badge—an Australian performance sensation that progressed from the twin-carb KA/KB Sport to the ferocious KC/KE and KF/KH TX3 Turbo 4WD, packing a 1.6L/1.8L turbocharged DOHC engine, full-time four-wheel drive, and digital instruments. Sourcing shifted to Japan in 1994 with the imported KJ, KL, and KQ series before the model was succeeded by the Focus.",
    "australian_market_notes": "The Laser was the best-selling small car in Australia throughout the 1980s, repeatedly outselling the Toyota Corolla and Holden Gemini. The TX3 Turbo 4WD became an Australian rally weapon, dominating Group A and Group N showroom-stock rally championships in the hands of privateers and creating a genuine cult classic today.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "KA-KB",
            "generation_name": "KA / KB Laser",
            "years": {"start": 1981, "end": 1985},
            "body_styles": ["3-door hatchback", "5-door hatchback"],
            "platform": "Ford/Mazda BD platform",
            "ancap_rating": None,
            "summary": "First front-wheel-drive Laser built at Homebush, Sydney. Crisp European-inspired hatchback styling, 1.3L and 1.5L E-series engines, and the peppy Laser Sport.",
            "engines": [
                {
                    "engine_code": "Mazda-E5S-TwinCarb",
                    "name": "Ford / Mazda E5S 1.5L Twin-Carb Inline-4",
                    "displacement_cc": 1490,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 59.0,
                    "power_rpm": "5800",
                    "torque_nm": 115.0,
                    "torque_rpm": "3500",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "Twin-barrel downdraft carburettor; powers Laser Sport."
                }
            ],
            "badges": [
                {
                    "badge_name": "Laser Sport",
                    "years": {"start": 1981, "end": 1985},
                    "body_styles": ["3-door hatchback"],
                    "drivetrain": "FWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 7890,
                    "msrp_aud_max": 8990,
                    "fuel_consumption_l_100km": 7.4,
                    "kerb_weight_kg": 850,
                    "standard_features": ["1.5L twin-carb engine", "Rear tailgate spoiler", "Sports steering wheel and tachometer", "Front bucket seats with striped velour"],
                    "notes": "Precursor to the famous TX3."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Laser Sport",
                    "body_style": "3-door hatchback",
                    "engine_code": "Mazda-E5S-TwinCarb",
                    "transmission": "5-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 7890,
                    "power_kw": 59.0,
                    "torque_nm": 115.0,
                    "fuel_l_100km": 7.4,
                    "towing_braked_kg": 600,
                    "notes": "Featherweight 850 kg sporty Aussie hatch."
                }
            ]
        },
        {
            "series_code": "KC-KE",
            "generation_name": "KC / KE Laser & TX3 Turbo",
            "years": {"start": 1985, "end": 1990},
            "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan (Meteor)", "5-door wagon"],
            "platform": "Ford/Mazda BF platform",
            "ancap_rating": None,
            "summary": "Aerodynamic styling, Homebush production. Historic launch of the TX3 Turbo and TX3 Turbo 4WD with 100 kW B6T engine, digital instruments, and all-wheel drive.",
            "engines": [
                {
                    "engine_code": "Mazda-B6T-Laser",
                    "name": "Ford / Mazda B6T 1.6L DOHC 16V Turbo Inline-4",
                    "displacement_cc": 1598,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 100.0,
                    "power_rpm": "5500",
                    "torque_nm": 184.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "7.9:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "Water-cooled turbocharger, air-to-air intercooler, electronic fuel injection."
                }
            ],
            "badges": [
                {
                    "badge_name": "TX3 Turbo 4WD",
                    "years": {"start": 1987, "end": 1990},
                    "body_styles": ["3-door hatchback"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 24990,
                    "msrp_aud_max": 27990,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 1080,
                    "standard_features": [
                        "100 kW 1.6L DOHC 16V Turbo engine",
                        "Permanent full-time 4WD with central differential lock",
                        "Electronic liquid-crystal digital instrument cluster",
                        "Four-wheel disc brakes and sports alloy wheels",
                        "Dual rear spoilers and sports bucket seats"
                    ],
                    "notes": "Legendary pocket rally homologation missile."
                }
            ],
            "configurations": [
                {
                    "badge_name": "TX3 Turbo 4WD",
                    "body_style": "3-door hatchback",
                    "engine_code": "Mazda-B6T-Laser",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 24990,
                    "power_kw": 100.0,
                    "torque_nm": 184.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 800,
                    "notes": "All-wheel-drive 1.6L turbo hot hatch."
                }
            ]
        },
        {
            "series_code": "KF-KH",
            "generation_name": "KF / KH Laser & TX3 Turbo 4WD",
            "years": {"start": 1990, "end": 1994},
            "body_styles": ["3-door hatchback", "5-door hatchback", "4-door sedan"],
            "platform": "Ford/Mazda BG platform",
            "ancap_rating": 2,
            "summary": "Final Homebush Sydney-manufactured Laser. Distinctive quad round headlight front styling on TX3, packing the upgraded 117 kW 1.8L DOHC Turbo BP-T engine and full-time 4WD.",
            "engines": [
                {
                    "engine_code": "Mazda-BP-T-1.8L",
                    "name": "Ford / Mazda BP-T 1.8L DOHC 16V Turbo Inline-4",
                    "displacement_cc": 1839,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 117.0,
                    "power_rpm": "6500",
                    "torque_nm": 206.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "DOHC 16V",
                    "notes": "IHI VJ20 turbocharger, large front intercooler; 117 kW (157 hp)."
                }
            ],
            "badges": [
                {
                    "badge_name": "TX3 Turbo 4WD",
                    "years": {"start": 1990, "end": 1994},
                    "body_styles": ["3-door hatchback"],
                    "drivetrain": "4WD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 29990,
                    "msrp_aud_max": 33990,
                    "fuel_consumption_l_100km": 8.9,
                    "kerb_weight_kg": 1195,
                    "standard_features": [
                        "117 kW 1.8L DOHC Turbo engine",
                        "Permanent AWD with viscous-coupling center and rear limited-slip differential",
                        "Distinctive four round projector headlamps",
                        "15-inch alloy wheels and ABS brakes option",
                        "Sports bucket seats and leather steering wheel"
                    ],
                    "notes": "Pinnacle of Laser performance; 0-100 km/h in 7.4 seconds."
                }
            ],
            "configurations": [
                {
                    "badge_name": "TX3 Turbo 4WD",
                    "body_style": "3-door hatchback",
                    "engine_code": "Mazda-BP-T-1.8L",
                    "transmission": "5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 29990,
                    "power_kw": 117.0,
                    "torque_nm": 206.0,
                    "fuel_l_100km": 8.9,
                    "towing_braked_kg": 900,
                    "notes": "117 kW 1.8L Turbo AWD hot hatch."
                }
            ]
        }
    ]
}
