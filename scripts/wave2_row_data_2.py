"""
Wave 2 Deep-Dive Models Part 2 (Models 9 to 16):
9. audi/q5-sq5
10. porsche/911
11. porsche/cayenne-macan
12. volvo/240-850
13. saab/900-9-3
14. skoda/octavia
15. peugeot/205-308-gti
16. renault/clio-megane-rs
"""
from typing import Dict, Any

WAVE2_MODELS_PART2: Dict[str, Dict[str, Any]] = {
    "audi/q5-sq5": {
        "make_slug": "audi",
        "model_slug": "q5-sq5",
        "name": "Q5 & SQ5",
        "vehicle_type": "Medium Luxury SUV",
        "segment": "Medium Luxury SUV",
        "years_sold_au": {"start": 2009, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Audi's best-selling luxury SUV in Australia. Built on the longitudinal MLB platform with quattro permanent all-wheel drive, the Q5 balanced executive prestige with family versatility, while the twin-turbo diesel SQ5 BiTDI became an unprecedented cult sales sensation in Australia.",
        "australian_market_notes": "First arrived in Australia in March 2009 (8R). In 2013, Audi launched the SQ5 TDI powered by a 230kW/650Nm 3.0L twin-turbo diesel V6. Australia immediately became the second-highest volume market for SQ5 globally per capita, accounting for over a third of all Australian Q5 sales.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "8R",
                "generation_name": "Q5 & SQ5 First Generation (Typ 8R)",
                "years": {"start": 2009, "end": "2017"},
                "body_styles": ["5-door SUV"],
                "platform": "Volkswagen Group MLB",
                "ancap_rating": "5 stars",
                "summary": "First-generation premium mid-size SUV featuring longitudinal engines, quattro AWD, 2.0 TDI/TFSI, 3.0 TDI, and the market-defining SQ5 TDI with a 230kW/240kW 650Nm twin-turbo diesel V6 and sound actuator exhaust.",
                "engines": [
                    {
                        "engine_code": "CGQB",
                        "name": "3.0L BiTDI Twin-Turbo Diesel V6 (SQ5)",
                        "displacement_cc": 2967,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 230,
                        "power_rpm": "3900-4500",
                        "torque_nm": 650,
                        "torque_rpm": "1450-2800",
                        "compression_ratio": "16.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Sequential twin-turbo system with exhaust sound actuator; later upgraded to 240kW SQ5 Plus."
                    },
                    {
                        "engine_code": "CDNC",
                        "name": "2.0L TFSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 155,
                        "power_rpm": "4300-6000",
                        "torque_nm": 350,
                        "torque_rpm": "1500-4200",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Core 4-cylinder petrol powertrain paired with 7-speed S tronic / 8-speed tiptronic."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "2.0 TFSI quattro",
                        "years": {"start": 2009, "end": 2017},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic", "8-speed tiptronic"],
                        "msrp_aud_min": 59900,
                        "msrp_aud_max": 66200,
                        "fuel_consumption_l_100km": 7.9,
                        "kerb_weight_kg": 1750,
                        "standard_features": ["18-inch alloy wheels", "Leather upholstery", "MMI navigation", "quattro permanent AWD", "Tri-zone climate control"],
                        "notes": "Core luxury SUV."
                    },
                    {
                        "badge_name": "SQ5 TDI",
                        "years": {"start": 2013, "end": 2017},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed tiptronic"],
                        "msrp_aud_min": 89400,
                        "msrp_aud_max": 93900,
                        "fuel_consumption_l_100km": 6.8,
                        "kerb_weight_kg": 1920,
                        "standard_features": ["20-inch 5-parallel-spoke alloys", "S sports suspension (30mm lower)", "Fine Nappa leather S sport seats", "Quad oval exhaust tips with active sound", "Xenon plus headlights"],
                        "notes": "0-100km/h in 5.1s. Huge Australian sales smash hit."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "SQ5 TDI",
                        "body_style": "5-door SUV",
                        "engine_code": "CGQB",
                        "transmission": "8-speed tiptronic",
                        "drivetrain": "AWD",
                        "years_start": 2013,
                        "years_end": 2017,
                        "msrp_aud": 89400,
                        "power_kw": 230,
                        "torque_nm": 650,
                        "fuel_l_100km": 6.8,
                        "towing_braked_kg": 2000,
                        "notes": "230kW twin-turbo diesel performance SUV."
                    }
                ]
            },
            {
                "series_code": "FY",
                "generation_name": "Q5 & SQ5 Second Generation (Typ FY)",
                "years": {"start": 2017, "end": "Present"},
                "body_styles": ["5-door SUV", "5-door Sportback"],
                "platform": "Volkswagen Group MLB evo",
                "ancap_rating": "5 stars",
                "summary": "Built on MLB evo platform with up to 90kg weight reduction. Features quattro ultra AWD, Virtual Cockpit, 45 TFSI, and the SQ5 TDI with 48V electric powered compressor (EPC) delivering 251kW and 700Nm.",
                "engines": [
                    {
                        "engine_code": "DECA",
                        "name": "3.0L V6 Turbo Diesel with 48V EPC (SQ5 TDI)",
                        "displacement_cc": 2967,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged with 48V Electric Powered Compressor",
                        "fuel_type": "Diesel",
                        "power_kw": 251,
                        "power_rpm": "3800-3950",
                        "torque_nm": 700,
                        "torque_rpm": "1750-3250",
                        "compression_ratio": "16.3:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Electric compressor spools in 250 milliseconds eliminating turbo lag."
                    },
                    {
                        "engine_code": "CWGD",
                        "name": "3.0L V6 Turbo Petrol (SQ5 TFSI)",
                        "displacement_cc": 2995,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 260,
                        "power_rpm": "5400-6400",
                        "torque_nm": 500,
                        "torque_rpm": "1370-4500",
                        "compression_ratio": "11.2:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Twin-scroll turbo mounted inside 90-degree vee."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "45 TFSI quattro",
                        "years": {"start": 2017, "end": "Present"},
                        "body_styles": ["5-door SUV", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic"],
                        "msrp_aud_min": 69900,
                        "msrp_aud_max": 82800,
                        "fuel_consumption_l_100km": 7.3,
                        "kerb_weight_kg": 1825,
                        "standard_features": ["19-inch alloys", "Audi Virtual Cockpit Plus", "quattro ultra technology", "Wireless Apple CarPlay"],
                        "notes": "Volume Australian luxury seller."
                    },
                    {
                        "badge_name": "SQ5 TDI / Sportback",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["5-door SUV", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed tiptronic"],
                        "msrp_aud_min": 104900,
                        "msrp_aud_max": 116400,
                        "fuel_consumption_l_100km": 7.0,
                        "kerb_weight_kg": 2010,
                        "standard_features": ["21-inch Audi Sport wheels", "Adaptive air suspension", "Matrix LED headlights with OLED taillights", "Bang & Olufsen 3D sound", "quattro sport rear differential"],
                        "notes": "0-100km/h in 5.1s. 700Nm diesel rocket."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "SQ5 TDI / Sportback",
                        "body_style": "5-door SUV",
                        "engine_code": "DECA",
                        "transmission": "8-speed tiptronic",
                        "drivetrain": "AWD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 110400,
                        "power_kw": 251,
                        "torque_nm": 700,
                        "fuel_l_100km": 7.0,
                        "towing_braked_kg": 2000,
                        "notes": "700Nm electric compressor turbo-diesel SUV."
                    }
                ]
            }
        ]
    },

    "porsche/911": {
        "make_slug": "porsche",
        "model_slug": "911",
        "name": "911 & 356",
        "vehicle_type": "Sports Car / Coupe / Cabriolet / Targa",
        "segment": "High Performance Sports Car",
        "years_sold_au": {"start": 1951, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The definitive rear-engine sports car. Australia boasts one of the most historic ties to Porsche in the world: Melbourne businessman Norman Hamilton secured the Australian concession in 1951, importing two 356s that represented the first right-hand drive Porsches ever made. Since the 911's local launch in 1965, it has defined sports car perfection through air-cooled and water-cooled eras, culminating in legendary Turbo, GT3, and GT3 RS icons.",
        "australian_market_notes": "In late 1951, Norman Hamilton brought the first two RHD 356 coupes to Australia (chassis 10517 and 10518). In motorsport, Jim Richards won multiple Australian Targa and touring car events in 911s. Australia consistently registers one of the world's highest proportions of Porsche GT cars (GT3, GT3 RS, GT2 RS) per capita.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "356 & Classic 911",
                "generation_name": "Porsche 356 & Early 911 Classic",
                "years": {"start": 1951, "end": 1973},
                "body_styles": ["Coupe", "Speedster / Cabriolet", "Targa"],
                "platform": "Porsche 356 / 911 Classic",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "From the world's first RHD 356 delivered in Melbourne in 1951 to the arrival of the 911 in 1965 with 2.0L, 2.2L, 2.4L flat-sixes and the homologation 1973 Carrera RS 2.7.",
                "engines": [
                    {
                        "engine_code": "911/01",
                        "name": "2.0L Air-Cooled Flat-6",
                        "displacement_cc": 1991,
                        "displacement_litres": 2.0,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 96,
                        "power_rpm": "6100",
                        "torque_nm": 174,
                        "torque_rpm": "4200",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "SOHC per bank 12-valve",
                        "notes": "Twin triple-throat Solex/Weber carburettors, dry sump lubrication."
                    },
                    {
                        "engine_code": "911/83",
                        "name": "2.7L Mechanical Fuel Injected Flat-6 (RS)",
                        "displacement_cc": 2687,
                        "displacement_litres": 2.7,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 154,
                        "power_rpm": "6300",
                        "torque_nm": 255,
                        "torque_rpm": "5100",
                        "compression_ratio": "8.5:1",
                        "valvetrain": "SOHC per bank 12-valve",
                        "notes": "Bosch mechanical fuel injection; ducktail rear spoiler homologation hero."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "911 2.0 / 2.4",
                        "years": {"start": 1965, "end": 1973},
                        "body_styles": ["Coupe", "Targa"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual (901/915)", "4-speed Sportomatic"],
                        "msrp_aud_min": 6990,
                        "msrp_aud_max": 14500,
                        "fuel_consumption_l_100km": 11.2,
                        "kerb_weight_kg": 1050,
                        "standard_features": ["Fuchs alloy wheels", "VDO green-dial instrumentation", "Four-wheel disc brakes", "Leatherette interior"],
                        "notes": "The birth of the 911 legend in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "911 2.0 / 2.4",
                        "body_style": "Coupe",
                        "engine_code": "911/01",
                        "transmission": "5-speed manual (901/915)",
                        "drivetrain": "RWD",
                        "years_start": 1965,
                        "years_end": 1969,
                        "msrp_aud": 7990,
                        "power_kw": 96,
                        "torque_nm": 174,
                        "fuel_l_100km": 11.2,
                        "towing_braked_kg": 600,
                        "notes": "Early short-wheelbase Australian delivered 911 Coupe."
                    }
                ]
            },
            {
                "series_code": "930",
                "generation_name": "911 G-Series & 930 Turbo",
                "years": {"start": 1974, "end": 1989},
                "body_styles": ["Coupe", "Targa", "Cabriolet"],
                "platform": "Porsche 911 G-Series",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Impact bumpers, 2.7L, 3.0L SC, 3.2 Carrera, and the iconic 930 Turbo (3.0L and 3.3L Turbo 'Widowmaker') with flared wheel arches and tea-tray spoiler.",
                "engines": [
                    {
                        "engine_code": "930/60",
                        "name": "3.3L Turbo Flat-6 (930 Turbo)",
                        "displacement_cc": 3299,
                        "displacement_litres": 3.3,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 221,
                        "power_rpm": "5500",
                        "torque_nm": 412,
                        "torque_rpm": "4000",
                        "compression_ratio": "7.0:1",
                        "valvetrain": "SOHC per bank 12-valve",
                        "notes": "Air-to-air intercooler under tea-tray rear spoiler; KKK turbocharger."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "930 Turbo 3.3",
                        "years": {"start": 1978, "end": 1989},
                        "body_styles": ["Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual (930)", "5-speed manual (G50 1989)"],
                        "msrp_aud_min": 72500,
                        "msrp_aud_max": 185000,
                        "fuel_consumption_l_100km": 14.5,
                        "kerb_weight_kg": 1335,
                        "standard_features": ["Flared turbo bodywork", "Tea-tray whale tail spoiler", "16-inch Fuchs alloys", "Four-piston 917-derived brakes", "Full leather interior"],
                        "notes": "0-100km/h in 5.2s. Poster supercar of a generation."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "930 Turbo 3.3",
                        "body_style": "Coupe",
                        "engine_code": "930/60",
                        "transmission": "4-speed manual (930)",
                        "drivetrain": "RWD",
                        "years_start": 1978,
                        "years_end": 1988,
                        "msrp_aud": 95000,
                        "power_kw": 221,
                        "torque_nm": 412,
                        "fuel_l_100km": 14.5,
                        "towing_braked_kg": 800,
                        "notes": "3.3-litre intercooled 930 Turbo Coupe."
                    }
                ]
            },
            {
                "series_code": "993",
                "generation_name": "911 Generation 993 (Last Air-Cooled)",
                "years": {"start": 1994, "end": 1998},
                "body_styles": ["Coupe", "Cabriolet", "Targa"],
                "platform": "Porsche 993",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The holy grail of air-cooled 911s. Redesigned multi-link LSA aluminum rear suspension, Carrera, widebody Carrera 4S, and the twin-turbo all-wheel-drive 993 Turbo producing 300kW.",
                "engines": [
                    {
                        "engine_code": "M64/60",
                        "name": "3.6L Twin-Turbo Flat-6 (993 Turbo)",
                        "displacement_cc": 3600,
                        "displacement_litres": 3.6,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 300,
                        "power_rpm": "5750",
                        "torque_nm": 540,
                        "torque_rpm": "4500",
                        "compression_ratio": "8.0:1",
                        "valvetrain": "SOHC per bank 12-valve",
                        "notes": "Twin KKK K16 turbochargers; last air-cooled Turbo engine."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "993 Turbo",
                        "years": {"start": 1995, "end": 1998},
                        "body_styles": ["Coupe"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 269000,
                        "msrp_aud_max": 289000,
                        "fuel_consumption_l_100km": 13.8,
                        "kerb_weight_kg": 1500,
                        "standard_features": ["18-inch hollow-spoke Technology alloys", "Permanent AWD with viscous coupling", "Fixed rear bi-plane spoiler", "Brembo 4-piston brakes in red"],
                        "notes": "0-100km/h in 4.5s. Crown jewel of modern Porsche collecting."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "993 Turbo",
                        "body_style": "Coupe",
                        "engine_code": "M64/60",
                        "transmission": "6-speed manual",
                        "drivetrain": "AWD",
                        "years_start": 1995,
                        "years_end": 1998,
                        "msrp_aud": 279000,
                        "power_kw": 300,
                        "torque_nm": 540,
                        "fuel_l_100km": 13.8,
                        "towing_braked_kg": 800,
                        "notes": "Air-cooled twin-turbo all-wheel drive flagship."
                    }
                ]
            },
            {
                "series_code": "997",
                "generation_name": "911 Generation 997",
                "years": {"start": 2005, "end": 2012},
                "body_styles": ["Coupe", "Cabriolet", "Targa", "Speedster"],
                "platform": "Porsche 997",
                "ancap_rating": "5 stars",
                "summary": "Restored the beloved round headlights. Introduced Direct Fuel Injection (DFI) and Porsche Doppelkupplung (PDK) dual-clutch transmission in 997.2, alongside the Mezger-engined 997 Turbo, GT3, and GT3 RS.",
                "engines": [
                    {
                        "engine_code": "M97/77",
                        "name": "3.8L Mezger Flat-6 (GT3 RS)",
                        "displacement_cc": 3797,
                        "displacement_litres": 3.8,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 331,
                        "power_rpm": "7900",
                        "torque_nm": 430,
                        "torque_rpm": "6750",
                        "compression_ratio": "12.2:1",
                        "valvetrain": "DOHC 24-valve VarioCam",
                        "notes": "Mezger competition engine, titanium conrods, 8500rpm rev limit."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "911 GT3 / GT3 RS",
                        "years": {"start": 2006, "end": 2012},
                        "body_styles": ["Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 269000,
                        "msrp_aud_max": 335000,
                        "fuel_consumption_l_100km": 12.8,
                        "kerb_weight_kg": 1375,
                        "standard_features": ["Carbon fibre rear wing", "Single-mass flywheel option", "Clubsport roll cage", "PASM active suspension"],
                        "notes": "Pure motorsport homologation perfection."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "911 GT3 / GT3 RS",
                        "body_style": "Coupe",
                        "engine_code": "M97/77",
                        "transmission": "6-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 2009,
                        "years_end": 2012,
                        "msrp_aud": 319000,
                        "power_kw": 331,
                        "torque_nm": 430,
                        "fuel_l_100km": 12.8,
                        "towing_braked_kg": 0,
                        "notes": "Naturally aspirated 8500rpm Mezger road racer."
                    }
                ]
            },
            {
                "series_code": "992",
                "generation_name": "911 Generation 992",
                "years": {"start": 2019, "end": "Present"},
                "body_styles": ["Coupe", "Cabriolet", "Targa", "Dakar"],
                "platform": "Porsche MMB",
                "ancap_rating": "5 stars",
                "summary": "Current apex of 911 development. Widebody architecture across all models, wet mode acoustic sensors, Turbo S (478kW/800Nm), Carrera GTS T-Hybrid (398kW), and the track-dominating GT3 RS with swan-neck active DRS aerodynamics.",
                "engines": [
                    {
                        "engine_code": "DKMB",
                        "name": "3.7L Twin-Turbo Flat-6 (Turbo S)",
                        "displacement_cc": 3745,
                        "displacement_litres": 3.7,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 478,
                        "power_rpm": "6750",
                        "torque_nm": 800,
                        "torque_rpm": "2500-4000",
                        "compression_ratio": "8.7:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Variable turbine geometry (VTG) twin turbochargers."
                    },
                    {
                        "engine_code": "DMC",
                        "name": "4.0L Naturally Aspirated Flat-6 (GT3 RS)",
                        "displacement_cc": 3996,
                        "displacement_litres": 4.0,
                        "cylinders": 6,
                        "configuration": "Flat-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 386,
                        "power_rpm": "8500",
                        "torque_nm": 465,
                        "torque_rpm": "6300",
                        "compression_ratio": "13.3:1",
                        "valvetrain": "DOHC 24-valve with rigid valvetrain",
                        "notes": "Individual throttle butterflies, dry sump with separate oil tank, 9000rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "911 Turbo S",
                        "years": {"start": 2020, "end": "Present"},
                        "body_styles": ["Coupe", "Cabriolet"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed PDK"],
                        "msrp_aud_min": 473500,
                        "msrp_aud_max": 540000,
                        "fuel_consumption_l_100km": 11.5,
                        "kerb_weight_kg": 1640,
                        "standard_features": ["PCCB carbon ceramic brakes (10-piston front)", "Active aerodynamics (front spoiler & rear wing)", "PASM sport chassis", "Center-lock forged wheels"],
                        "notes": "0-100km/h in 2.7s. 650hp all-weather missile."
                    },
                    {
                        "badge_name": "911 GT3 RS",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["7-speed PDK"],
                        "msrp_aud_min": 500200,
                        "msrp_aud_max": 550000,
                        "fuel_consumption_l_100km": 13.4,
                        "kerb_weight_kg": 1450,
                        "standard_features": ["Active swan-neck rear wing with DRS", "Central radiator concept from 911 RSR", "Front diffuser and louvres generating 860kg downforce", "Steering wheel rotary switches for differential and suspension setup"],
                        "notes": "0-100km/h in 3.2s. Road-legal GT race car for the track."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "911 Turbo S",
                        "body_style": "Coupe",
                        "engine_code": "DKMB",
                        "transmission": "8-speed PDK",
                        "drivetrain": "AWD",
                        "years_start": 2020,
                        "years_end": "Present",
                        "msrp_aud": 498500,
                        "power_kw": 478,
                        "torque_nm": 800,
                        "fuel_l_100km": 11.5,
                        "towing_braked_kg": 0,
                        "notes": "478kW twin-turbo all-wheel drive benchmark."
                    },
                    {
                        "badge_name": "911 GT3 RS",
                        "body_style": "Coupe",
                        "engine_code": "DMC",
                        "transmission": "7-speed PDK",
                        "drivetrain": "RWD",
                        "years_start": 2023,
                        "years_end": "Present",
                        "msrp_aud": 500200,
                        "power_kw": 386,
                        "torque_nm": 465,
                        "fuel_l_100km": 13.4,
                        "towing_braked_kg": 0,
                        "notes": "386kW 9000rpm naturally aspirated downforce weapon."
                    }
                ]
            }
        ]
    },

    "porsche/cayenne-macan": {
        "make_slug": "porsche",
        "model_slug": "cayenne-macan",
        "name": "Cayenne & Macan",
        "vehicle_type": "Luxury Performance SUV",
        "segment": "Medium & Large Luxury SUV",
        "years_sold_au": {"start": 2003, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The commercial lifeblood of modern Porsche. When introduced in 2003, the Cayenne proved that a true Porsche could haul five adults and conquer the Simpson Desert, while setting racetrack lap records. The smaller Macan arrived in 2014, quickly becoming Porsche's best-selling model in Australia, and leading Porsche's electric transformation with the Macan EV.",
        "australian_market_notes": "The Cayenne arrived in Australia in mid-2003 to initial skepticism that rapidly dissolved as buyers experienced its astonishing handling and 3,500kg towing prowess. In 2014, the Macan debuted, quickly capturing huge waiting lists in Sydney and Melbourne.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "955/957",
                "generation_name": "Cayenne First Generation (Typ 955/957)",
                "years": {"start": 2003, "end": 2010},
                "body_styles": ["5-door SUV"],
                "platform": "Volkswagen Group PL71",
                "ancap_rating": "Unrated",
                "summary": "First-generation Cayenne featuring permanent 4WD with low-range transfer case, center and rear locking differentials, air suspension, Cayenne S 4.5/4.8 V8, and the earth-shattering Cayenne Turbo and Turbo S.",
                "engines": [
                    {
                        "engine_code": "M48/50",
                        "name": "4.5L Twin-Turbo V8 (Cayenne Turbo)",
                        "displacement_cc": 4511,
                        "displacement_litres": 4.5,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 331,
                        "power_rpm": "6000",
                        "torque_nm": 620,
                        "torque_rpm": "2250-4750",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "DOHC 32-valve VarioCam",
                        "notes": "Twin turbochargers with twin intercoolers; 0-100km/h in 5.6s."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Cayenne Turbo",
                        "years": {"start": 2003, "end": 2010},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed Tiptronic S"],
                        "msrp_aud_min": 207900,
                        "msrp_aud_max": 235000,
                        "fuel_consumption_l_100km": 15.7,
                        "kerb_weight_kg": 2355,
                        "standard_features": ["PASM air suspension with ride height adjustment", "Low range transfer case with center diff lock", "19-inch Turbo alloys", "Bose surround sound", "Leather upholstery"],
                        "notes": "The super-SUV pioneer that rescued Porsche's balance sheet."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Cayenne Turbo",
                        "body_style": "5-door SUV",
                        "engine_code": "M48/50",
                        "transmission": "6-speed Tiptronic S",
                        "drivetrain": "AWD",
                        "years_start": 2003,
                        "years_end": 2007,
                        "msrp_aud": 209000,
                        "power_kw": 331,
                        "torque_nm": 620,
                        "fuel_l_100km": 15.7,
                        "towing_braked_kg": 3500,
                        "notes": "Heavy-duty off-road capable 331kW super-SUV."
                    }
                ]
            },
            {
                "series_code": "9Y0",
                "generation_name": "Cayenne Third Generation (Typ 9Y0 & Turbo GT)",
                "years": {"start": 2018, "end": "Present"},
                "body_styles": ["5-door SUV", "5-door Coupé"],
                "platform": "Volkswagen Group MLB evo",
                "ancap_rating": "5 stars",
                "summary": "Lightweight aluminum chassis MLB evo, rear-axle steering, 48V active anti-roll stabilization, and the record-setting Cayenne Turbo GT Coupé with 471kW 4.0L twin-turbo V8.",
                "engines": [
                    {
                        "engine_code": "DWD",
                        "name": "4.0L Twin-Turbo V8 (Turbo GT)",
                        "displacement_cc": 3996,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 471,
                        "power_rpm": "6000",
                        "torque_nm": 850,
                        "torque_rpm": "2300-4500",
                        "compression_ratio": "9.7:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Upgraded crankshaft, conrods, pistons, and titanium central exhaust."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Cayenne Turbo GT Coupé",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["5-door Coupé"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed Tiptronic S"],
                        "msrp_aud_min": 336100,
                        "msrp_aud_max": 366200,
                        "fuel_consumption_l_100km": 12.6,
                        "kerb_weight_kg": 2220,
                        "standard_features": ["22-inch GT Design wheels in Neodyme", "Carbon ceramic brakes (PCCB)", "Titanium sports exhaust with center tips", "Carbon fibre roof", "Alcantara interior with contrast stitching"],
                        "notes": "0-100km/h in 3.3s. Nurburgring production SUV lap record."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Cayenne Turbo GT Coupé",
                        "body_style": "5-door Coupé",
                        "engine_code": "DWD",
                        "transmission": "8-speed Tiptronic S",
                        "drivetrain": "AWD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 351900,
                        "power_kw": 471,
                        "torque_nm": 850,
                        "fuel_l_100km": 12.6,
                        "towing_braked_kg": 3500,
                        "notes": "471kW track-tuned hyper-SUV Coupé."
                    }
                ]
            },
            {
                "series_code": "95B",
                "generation_name": "Macan First Generation (Typ 95B)",
                "years": {"start": 2014, "end": 2024},
                "body_styles": ["5-door SUV"],
                "platform": "Volkswagen Group MLB (Porsche modified)",
                "ancap_rating": "5 stars",
                "summary": "Porsche's mega-volume mid-size SUV. Heavily re-engineered MLB chassis with rear-biased all-wheel drive, dual-clutch PDK, 2.0T four-cylinder, 3.0T/2.9T twin-turbo V6, Macan GTS, and Macan Turbo.",
                "engines": [
                    {
                        "engine_code": "DGR",
                        "name": "2.9L Twin-Turbo V6 (Macan GTS)",
                        "displacement_cc": 2894,
                        "displacement_litres": 2.9,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 324,
                        "power_rpm": "5700-6600",
                        "torque_nm": 550,
                        "torque_rpm": "1900-5600",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Hot-V twin-turbo engine producing 440hp in flagship Macan GTS."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Macan GTS",
                        "years": {"start": 2016, "end": 2024},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed PDK"],
                        "msrp_aud_min": 109500,
                        "msrp_aud_max": 141700,
                        "fuel_consumption_l_100km": 9.9,
                        "kerb_weight_kg": 1960,
                        "standard_features": ["21-inch RS Spyder Design alloys", "GTS sport air suspension (10mm lowered)", "Sport Chrono package", "Porsche Surface Coated Brakes (PSCB)", "GTS sports seats in leather and Race-Tex"],
                        "notes": "0-100km/h in 4.3s. The driver's medium luxury SUV benchmark."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Macan GTS",
                        "body_style": "5-door SUV",
                        "engine_code": "DGR",
                        "transmission": "7-speed PDK",
                        "drivetrain": "AWD",
                        "years_start": 2021,
                        "years_end": 2024,
                        "msrp_aud": 133900,
                        "power_kw": 324,
                        "torque_nm": 550,
                        "fuel_l_100km": 9.9,
                        "towing_braked_kg": 2400,
                        "notes": "324kW twin-turbo sports flagship Macan."
                    }
                ]
            },
            {
                "series_code": "XAB",
                "generation_name": "Macan Electric (Typ XAB)",
                "years": {"start": 2024, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "Premium Platform Electric (PPE)",
                "ancap_rating": "5 stars",
                "summary": "Next-generation dedicated electric Macan built on the 800V PPE platform. Equipped with 100kWh lithium-ion battery, dual permanently excited synchronous electric motors, rear-axle steering, and up to 470kW (639hp) and 1,130Nm in the Macan Turbo EV.",
                "engines": [
                    {
                        "engine_code": "PPE-DUAL",
                        "name": "Dual Permanent Magnet Electric Motors (Macan Turbo EV)",
                        "displacement_cc": 0,
                        "displacement_litres": 0.0,
                        "cylinders": 0,
                        "configuration": "Electric",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Electric",
                        "power_kw": 470,
                        "power_rpm": "Overboost",
                        "torque_nm": 1130,
                        "torque_rpm": "0-6000",
                        "compression_ratio": "N/A",
                        "valvetrain": "N/A",
                        "notes": "100kWh gross battery; 270kW DC ultra-rapid 800V charging (10-80% in 21 mins)."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Macan Turbo EV",
                        "years": {"start": 2024, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["1-speed direct drive"],
                        "msrp_aud_min": 180100,
                        "msrp_aud_max": 205000,
                        "fuel_consumption_l_100km": 0.0,
                        "kerb_weight_kg": 2405,
                        "standard_features": ["21-inch Macan Turbo wheels", "Porsche Torque Vectoring Plus (PTV Plus)", "Air suspension with PASM", "Curved OLED instrument cluster", "Augmented reality head-up display"],
                        "notes": "0-100km/h in 3.3s. High-voltage EV performance hero."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Macan Turbo EV",
                        "body_style": "5-door SUV",
                        "engine_code": "PPE-DUAL",
                        "transmission": "1-speed direct drive",
                        "drivetrain": "AWD",
                        "years_start": 2024,
                        "years_end": "Present",
                        "msrp_aud": 180100,
                        "power_kw": 470,
                        "torque_nm": 1130,
                        "fuel_l_100km": 0.0,
                        "towing_braked_kg": 2000,
                        "notes": "470kW electric all-wheel drive SUV with 1130Nm."
                    }
                ]
            }
        ]
    },

    "volvo/240-850": {
        "make_slug": "volvo",
        "model_slug": "240-850",
        "name": "240 & 850 Series",
        "vehicle_type": "Sedan / Wagon",
        "segment": "Medium / Large Executive Car",
        "years_sold_au": {"start": 1975, "end": 1997},
        "locally_built": True,
        "assembly_plants_au": ["Clayton, Victoria (1975-1988)"],
        "overview": "The twin legends that transformed Volvo's reputation in Australia. The 240 Series was assembled locally at Clayton, Victoria, setting world safety standards and winning the 1986 Australian Touring Car Championship as the 'Flying Brick'. Its successor, the 850 Series, introduced front-wheel drive transverse 5-cylinder performance, celebrated by the limited-edition 850 T-5R and the 850 Super Tourers raced by Peter Brock and Jim Richards.",
        "australian_market_notes": "Locally assembled at Clayton, Victoria by Volvo Australia from 1975 to 1988. In 1986, Kiwi driver Robbie Francevic drove the Mark Petch/Volvo Dealer Team 240 Turbo to outright victory in the Australian Touring Car Championship—the first and only turbo Volvo to win the ATCC. A decade later in 1996, Peter Brock and Jim Richards famously piloted factory Volvo 850 sedans in the Australian Super Touring Championship and Bathurst 1000.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "240 Series",
                "generation_name": "Volvo 240 Series (242 / 244 / 245)",
                "years": {"start": 1975, "end": 1993},
                "body_styles": ["2-door sedan (242)", "4-door sedan (244)", "5-door wagon (245)"],
                "platform": "Volvo 200 Series",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Clayton-assembled Swedish icon renowned for legendary longevity and steel safety cage. Featured B21/B23/B230 'redblock' engines, 242 GT sports coupe, and the Group A 240 Turbo that conquered Australian touring car racing.",
                "engines": [
                    {
                        "engine_code": "B230E",
                        "name": "2.3L SOHC 'Redblock' Inline-4",
                        "displacement_cc": 2316,
                        "displacement_litres": 2.3,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 96,
                        "power_rpm": "5400",
                        "torque_nm": 190,
                        "torque_rpm": "2750",
                        "compression_ratio": "10.3:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "Bosch K-Jetronic / LH-Jetronic fuel injection;cast iron block of legendary durability."
                    },
                    {
                        "engine_code": "B21ET",
                        "name": "2.1L SOHC Turbo 'Redblock' (Group A)",
                        "displacement_cc": 2127,
                        "displacement_litres": 2.1,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 114,
                        "power_rpm": "5200",
                        "torque_nm": 250,
                        "torque_rpm": "3500",
                        "compression_ratio": "7.5:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "Garrett turbocharger; Group A race engines developed over 250kW (340hp)."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "244 GL / GLE",
                        "years": {"start": 1975, "end": 1993},
                        "body_styles": ["4-door sedan", "5-door wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual with electric overdrive", "3-speed automatic", "4-speed automatic"],
                        "msrp_aud_min": 8990,
                        "msrp_aud_max": 38990,
                        "fuel_consumption_l_100km": 10.4,
                        "kerb_weight_kg": 1340,
                        "standard_features": ["Four-wheel disc brakes with dual triangular circuits", "Heated front seats", "Power steering", "Plush velour upholstery"],
                        "notes": "Assembled in Melbourne. Australian family and professional favorite."
                    },
                    {
                        "badge_name": "242 GT",
                        "years": {"start": 1979, "end": 1980},
                        "body_styles": ["2-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual with overdrive"],
                        "msrp_aud_min": 14200,
                        "msrp_aud_max": 15500,
                        "fuel_consumption_l_100km": 11.2,
                        "kerb_weight_kg": 1360,
                        "standard_features": ["Silver metallic paint with black/red stripes", "Fog lamps in grille", "Heavy-duty anti-roll bars", "Corduroy sports seats with red cord piping"],
                        "notes": "Rare Australian-delivered homologation sports model."
                    },
                    {
                        "badge_name": "240 Turbo Group A 'Flying Brick'",
                        "years": {"start": 1985, "end": 1986},
                        "body_styles": ["2-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual (Getrag)"],
                        "msrp_aud_min": 45000,
                        "msrp_aud_max": 52000,
                        "fuel_consumption_l_100km": 13.5,
                        "kerb_weight_kg": 1280,
                        "standard_features": ["BBS alloy wheels", "Water injection", "Locking differential", "Rear bootlip spoiler"],
                        "notes": "Won the 1986 Australian Touring Car Championship driven by Robbie Francevic."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "244 GL / GLE",
                        "body_style": "4-door sedan",
                        "engine_code": "B230E",
                        "transmission": "4-speed automatic",
                        "drivetrain": "RWD",
                        "years_start": 1985,
                        "years_end": 1993,
                        "msrp_aud": 32900,
                        "power_kw": 96,
                        "torque_nm": 190,
                        "fuel_l_100km": 10.4,
                        "towing_braked_kg": 1500,
                        "notes": "Clayton-assembled executive sedan."
                    },
                    {
                        "badge_name": "240 Turbo Group A 'Flying Brick'",
                        "body_style": "2-door sedan",
                        "engine_code": "B21ET",
                        "transmission": "5-speed manual (Getrag)",
                        "drivetrain": "RWD",
                        "years_start": 1985,
                        "years_end": 1986,
                        "msrp_aud": 48000,
                        "power_kw": 114,
                        "torque_nm": 250,
                        "fuel_l_100km": 13.5,
                        "towing_braked_kg": 1200,
                        "notes": "ATCC championship winning touring car homologation model."
                    }
                ]
            },
            {
                "series_code": "850 Series",
                "generation_name": "Volvo 850 Series (GLT / T-5 / T-5R / R)",
                "years": {"start": 1992, "end": 1997},
                "body_styles": ["4-door sedan", "5-door wagon"],
                "platform": "Volvo P80",
                "ancap_rating": "4 stars",
                "summary": "Revolutionary front-wheel drive transverse 5-cylinder chassis featuring Side Impact Protection System (SIPS), Delta-link rear suspension, 850 GLT, 850 Turbo / T-5, the iconic Cream Yellow 850 T-5R, and the 184kW 850 R. Campaigned by Peter Brock in the Australian Super Touring Championship and Bathurst 1000.",
                "engines": [
                    {
                        "engine_code": "B5254S",
                        "name": "2.5L DOHC 20V Inline-5 (GLT)",
                        "displacement_cc": 2435,
                        "displacement_litres": 2.5,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 125,
                        "power_rpm": "6200",
                        "torque_nm": 220,
                        "torque_rpm": "3300",
                        "compression_ratio": "10.3:1",
                        "valvetrain": "DOHC 20-valve",
                        "notes": "Transverse all-aluminium 5-cylinder with distinct warble note."
                    },
                    {
                        "engine_code": "B5234T4",
                        "name": "2.3L High Output Turbo Inline-5 (850 R)",
                        "displacement_cc": 2319,
                        "displacement_litres": 2.3,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 184,
                        "power_rpm": "5400",
                        "torque_nm": 350,
                        "torque_rpm": "2400-5000",
                        "compression_ratio": "8.5:1",
                        "valvetrain": "DOHC 20-valve",
                        "notes": "Mitsubishi TD04HL-16T turbocharger; 250hp in 5-speed manual with Torsen LSD."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "850 GLT",
                        "years": {"start": 1992, "end": 1997},
                        "body_styles": ["4-door sedan", "5-door wagon"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 44950,
                        "msrp_aud_max": 59900,
                        "fuel_consumption_l_100km": 9.8,
                        "kerb_weight_kg": 1390,
                        "standard_features": ["Dual front airbags", "SIPS side-impact bags", "Climate control", "Leather steering wheel"],
                        "notes": "Pioneered side airbags in Australia."
                    },
                    {
                        "badge_name": "850 T-5R / 850 R",
                        "years": {"start": 1995, "end": 1997},
                        "body_styles": ["4-door sedan", "5-door wagon"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual (with Torsen LSD)", "4-speed automatic"],
                        "msrp_aud_min": 79900,
                        "msrp_aud_max": 84900,
                        "fuel_consumption_l_100km": 10.8,
                        "kerb_weight_kg": 1445,
                        "standard_features": ["17-inch 'Titan' anthracite / 'Volans' alloys", "Alcantara/leather sport seats", "Birch wood trim", "Lowered sports chassis", "Front lip and rear lip spoilers"],
                        "notes": "0-100km/h in 6.7s. High-performance cult hero driven by Peter Brock."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "850 T-5R / 850 R",
                        "body_style": "5-door wagon",
                        "engine_code": "B5234T4",
                        "transmission": "5-speed manual (with Torsen LSD)",
                        "drivetrain": "FWD",
                        "years_start": 1996,
                        "years_end": 1997,
                        "msrp_aud": 82900,
                        "power_kw": 184,
                        "torque_nm": 350,
                        "fuel_l_100km": 10.8,
                        "towing_braked_kg": 1600,
                        "notes": "184kW manual 850 R wagon with Torsen differential."
                    }
                ]
            }
        ]
    },

    "saab/900-9-3": {
        "make_slug": "saab",
        "model_slug": "900-9-3",
        "name": "900 & 9-3",
        "vehicle_type": "Sedan / Hatchback / Convertible / Wagon",
        "segment": "Medium Executive Sports Car",
        "years_sold_au": {"start": 1979, "end": 2011},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Born from jets. Saab brought Swedish aircraft engineering, wraparound windscreens, night panels, and turbocharging mastery to Australia across more than three decades. The Classic 900 Turbo established Saab's intellectual cool, followed by the lightning-quick 9-3 Viggen and the 206kW 2.8T Aero V6.",
        "australian_market_notes": "First sold in Australia in 1979 (Classic 900). The 900 Turbo Cabriolet became an icon of Australian coastal affluence and design distinction. The 9-3 Viggen—named after the Saab 37 Viggen fighter aircraft—became a rare Australian cult vehicle with 169kW through the front wheels.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Classic 900",
                "generation_name": "Saab 900 'Classic' Generation",
                "years": {"start": 1979, "end": 1993},
                "body_styles": ["3-door combi-coupe", "5-door combi-coupe", "4-door sedan", "2-door convertible"],
                "platform": "Saab 99/900",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Aircraft cockpit ergonomics, center ignition switch, longitudinal engine tilted backwards at 45 degrees over the gearbox. Highlighted by the 900 Turbo 16S / Aero with 129kW APC boost control and the beloved Convertible.",
                "engines": [
                    {
                        "engine_code": "B202XL",
                        "name": "2.0L 16V Turbo (Turbo 16S / Aero)",
                        "displacement_cc": 1985,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 129,
                        "power_rpm": "5300",
                        "torque_nm": 273,
                        "torque_rpm": "3000",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Automatic Performance Control (APC) knock sensor adjusting boost pressure to fuel octane."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "900 Turbo 16S / Aero",
                        "years": {"start": 1984, "end": 1993},
                        "body_styles": ["3-door combi-coupe", "2-door convertible"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 44900,
                        "msrp_aud_max": 79900,
                        "fuel_consumption_l_100km": 9.5,
                        "kerb_weight_kg": 1240,
                        "standard_features": ["Aero three-spoke alloy wheels", "Factory bodykit", "Leather upholstery", "Heated seats", "Sunroof"],
                        "notes": "Architects' and designers' dream car of the 1980s in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "900 Turbo 16S / Aero",
                        "body_style": "3-door combi-coupe",
                        "engine_code": "B202XL",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1984,
                        "years_end": 1993,
                        "msrp_aud": 52900,
                        "power_kw": 129,
                        "torque_nm": 273,
                        "fuel_l_100km": 9.5,
                        "towing_braked_kg": 1500,
                        "notes": "Classic 16-valve APC Turbo combi-coupe."
                    }
                ]
            },
            {
                "series_code": "9-3 OG",
                "generation_name": "Saab 9-3 First Generation & Viggen",
                "years": {"start": 1998, "end": 2002},
                "body_styles": ["3-door coupe", "5-door hatchback", "2-door convertible"],
                "platform": "GM2900 (heavily modified by Saab)",
                "ancap_rating": "4 stars",
                "summary": "Introduced over 1,100 mechanical improvements, Saab Active Head Restraints (SAHR), Night Panel blackout dash, and the ultra-rare 9-3 Viggen powered by the 169kW 2.3L High Output Turbo.",
                "engines": [
                    {
                        "engine_code": "B235R",
                        "name": "2.3L High Output Turbo (Viggen)",
                        "displacement_cc": 2290,
                        "displacement_litres": 2.3,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 169,
                        "power_rpm": "5500",
                        "torque_nm": 350,
                        "torque_rpm": "2500-4000",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Mitsubishi TD04HL turbocharger; Trionic 7 engine management."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "9-3 Viggen",
                        "years": {"start": 1999, "end": 2002},
                        "body_styles": ["3-door coupe", "5-door hatchback", "2-door convertible"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 78900,
                        "msrp_aud_max": 89900,
                        "fuel_consumption_l_100km": 9.9,
                        "kerb_weight_kg": 1395,
                        "standard_features": ["17-inch 5-spoke Viggen alloys", "Lightning Blue hero paint", "Rear wing spoiler (Cd reduced to 0.31)", "Two-tone leather sports seats with embossed Viggen delta wing logo", "Sport suspension"],
                        "notes": "0-100km/h in 6.4s. Named after the Saab 37 Viggen fighter jet."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "9-3 Viggen",
                        "body_style": "3-door coupe",
                        "engine_code": "B235R",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1999,
                        "years_end": 2002,
                        "msrp_aud": 81900,
                        "power_kw": 169,
                        "torque_nm": 350,
                        "fuel_l_100km": 9.9,
                        "towing_braked_kg": 1600,
                        "notes": "Fighter-jet inspired 169kW turbocharged coupe."
                    }
                ]
            },
            {
                "series_code": "9-3 SS/SC",
                "generation_name": "Saab 9-3 Sport Sedan, SportCombi & Turbo X",
                "years": {"start": 2003, "end": 2011},
                "body_styles": ["4-door Sport Sedan", "5-door SportCombi wagon", "2-door convertible"],
                "platform": "GM Epsilon",
                "ancap_rating": "5 stars",
                "summary": "Built on GM Epsilon platform with Saab-exclusive ReAxs passive rear-wheel steering. Highlighted by the Aero 2.8T V6 (up to 206kW) and the limited-edition all-wheel-drive Turbo X with Haldex XWD and eLSD.",
                "engines": [
                    {
                        "engine_code": "B284L/R",
                        "name": "2.8L 24V Turbo V6 (Aero / Turbo X)",
                        "displacement_cc": 2792,
                        "displacement_litres": 2.8,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 206,
                        "power_rpm": "5500",
                        "torque_nm": 400,
                        "torque_rpm": "2150-4500",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Twin-scroll water-cooled turbocharger, 60-degree all-aluminium vee."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "9-3 Aero 2.8T",
                        "years": {"start": 2005, "end": 2011},
                        "body_styles": ["4-door Sport Sedan", "5-door SportCombi wagon", "2-door convertible"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "6-speed Sentronic automatic"],
                        "msrp_aud_min": 69900,
                        "msrp_aud_max": 89900,
                        "fuel_consumption_l_100km": 10.2,
                        "kerb_weight_kg": 1580,
                        "standard_features": ["17/18-inch Aero alloys", "ReAxs passive rear steering", "Bose surround sound", "Sport leather seats", "Dual exhaust outlets"],
                        "notes": "Silky 2.8L turbo V6 sports sedan."
                    },
                    {
                        "badge_name": "9-3 Turbo X",
                        "years": {"start": 2008, "end": 2009},
                        "body_styles": ["4-door Sport Sedan", "5-door SportCombi wagon"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual", "6-speed automatic"],
                        "msrp_aud_min": 89900,
                        "msrp_aud_max": 94900,
                        "fuel_consumption_l_100km": 10.9,
                        "kerb_weight_kg": 1690,
                        "standard_features": ["Haldex Gen 4 XWD with electronic LSD", "Jet Black metallic exclusive paint", "19-inch turbine wheels", "Turbo boost gauge styled after Classic 900", "Brembo brakes"],
                        "notes": "0-100km/h in 5.7s. 30th anniversary tribute to the original 900 Turbo."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "9-3 Turbo X",
                        "body_style": "4-door Sport Sedan",
                        "engine_code": "B284L/R",
                        "transmission": "6-speed manual",
                        "drivetrain": "AWD",
                        "years_start": 2008,
                        "years_end": 2009,
                        "msrp_aud": 89900,
                        "power_kw": 206,
                        "torque_nm": 400,
                        "fuel_l_100km": 10.9,
                        "towing_braked_kg": 1600,
                        "notes": "206kW all-wheel drive XWD limited edition."
                    }
                ]
            }
        ]
    },

    "skoda/octavia": {
        "make_slug": "skoda",
        "model_slug": "octavia",
        "name": "Octavia",
        "vehicle_type": "Sedan (Liftback) / Wagon (Combi)",
        "segment": "Medium Car",
        "years_sold_au": {"start": 2007, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The intelligent family choice in Australia. Since spearheading Skoda's return to Australia in October 2007, the Octavia has won legions of loyal fans by combining Volkswagen Group engineering and Golf GTI drivetrains with cavernous boot space and 'Simply Clever' practical details. The Octavia RS Liftback and Combi wagon represent Australia's favorite value performance family express.",
        "australian_market_notes": "Skoda officially relaunched in Australia in October 2007 with the Octavia 1Z. The high-performance Octavia RS rapidly became the brand's best-selling model in Australia, regularly accounting for up to 40% of all Australian Octavia sales—the highest RS mix in the world.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "1Z",
                "generation_name": "Octavia Second Generation (Typ 1Z)",
                "years": {"start": 2007, "end": 2013},
                "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                "platform": "Volkswagen Group PQ35",
                "ancap_rating": "4 stars",
                "summary": "Relaunched Skoda to Australia in 2007. Featured 1.8 TSI, 2.0 TDI, rugged Octavia Scout 4x4 wagon, and the cult Octavia RS (2.0 TSI 147kW and 2.0 TDI 125kW).",
                "engines": [
                    {
                        "engine_code": "BWA/CCZA",
                        "name": "2.0L TSI Turbo Petrol (RS)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 147,
                        "power_rpm": "5100-6000",
                        "torque_nm": 280,
                        "torque_rpm": "1700-5000",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Golf GTI Mk5/Mk6 powertrain in a practical liftback or wagon."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Octavia RS 2.0 TSI",
                        "years": {"start": 2007, "end": 2013},
                        "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "6-speed DSG"],
                        "msrp_aud_min": 37990,
                        "msrp_aud_max": 41990,
                        "fuel_consumption_l_100km": 7.7,
                        "kerb_weight_kg": 1400,
                        "standard_features": ["18-inch Zenith / Neptune alloys", "RS sports bodykit", "VRS embroidered leather/alcantara seats", "Dual chrome exhaust tips", "Lowered sports suspension"],
                        "notes": "0-100km/h in 7.2s. Enormous 560L/580L boot."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Octavia RS 2.0 TSI",
                        "body_style": "5-door Combi wagon",
                        "engine_code": "BWA/CCZA",
                        "transmission": "6-speed DSG",
                        "drivetrain": "FWD",
                        "years_start": 2008,
                        "years_end": 2013,
                        "msrp_aud": 39990,
                        "power_kw": 147,
                        "torque_nm": 280,
                        "fuel_l_100km": 7.7,
                        "towing_braked_kg": 1400,
                        "notes": "Benchmark practical performance wagon."
                    }
                ]
            },
            {
                "series_code": "5E",
                "generation_name": "Octavia Third Generation (Typ 5E)",
                "years": {"start": 2013, "end": 2020},
                "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                "platform": "Volkswagen Group MQB",
                "ancap_rating": "5 stars",
                "summary": "Built on the MQB platform with 100kg weight reduction and massive 590L/610L boot. Powered by 103TSI, 110TSI, and the acclaimed Octavia RS (162TSI, 169TSI, and the flagship RS 245 with VAQ electronic front differential lock).",
                "engines": [
                    {
                        "engine_code": "DLBA",
                        "name": "2.0L TSI 180TSI Turbo Petrol (RS 245)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 180,
                        "power_rpm": "5000-6700",
                        "torque_nm": 370,
                        "torque_rpm": "1600-4300",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 Gen 3 paired with VAQ electro-mechanical front differential lock."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Octavia RS 245",
                        "years": {"start": 2017, "end": 2020},
                        "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "7-speed DSG"],
                        "msrp_aud_min": 43390,
                        "msrp_aud_max": 47090,
                        "fuel_consumption_l_100km": 6.5,
                        "kerb_weight_kg": 1425,
                        "standard_features": ["19-inch Vega gloss black alloys", "VAQ electronic locking front diff", "Alcantara/leather sport seats", "9.2-inch Columbus navigation", "Black design exterior pack"],
                        "notes": "0-100km/h in 6.6s. Widely praised by Australian automotive journalists."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Octavia RS 245",
                        "body_style": "5-door Combi wagon",
                        "engine_code": "DLBA",
                        "transmission": "7-speed DSG",
                        "drivetrain": "FWD",
                        "years_start": 2017,
                        "years_end": 2020,
                        "msrp_aud": 45490,
                        "power_kw": 180,
                        "torque_nm": 370,
                        "fuel_l_100km": 6.5,
                        "towing_braked_kg": 1600,
                        "notes": "180kW wagon with VAQ limited slip differential."
                    }
                ]
            },
            {
                "series_code": "NX",
                "generation_name": "Octavia Fourth Generation (Typ NX)",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                "platform": "Volkswagen Group MQB evo",
                "ancap_rating": "5 stars",
                "summary": "Sharp crystalline design, shift-by-wire DSG, Matrix LED headlights, class-leading 600L/640L boot, Style 110TSI, and the hero Octavia RS with 180kW/370Nm 2.0 TSI engine and standard VAQ differential.",
                "engines": [
                    {
                        "engine_code": "DNPA",
                        "name": "2.0L TSI 180TSI Turbo Petrol (RS)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 180,
                        "power_rpm": "5000-6500",
                        "torque_nm": 370,
                        "torque_rpm": "1600-4300",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 evo4 powertrain with standard VAQ front diff lock."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Octavia RS Liftback / Combi",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["5-door Liftback", "5-door Combi wagon"],
                        "drivetrain": "FWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 49090,
                        "msrp_aud_max": 57490,
                        "fuel_consumption_l_100km": 6.8,
                        "kerb_weight_kg": 1470,
                        "standard_features": ["19-inch Altair anthracite alloys", "Matrix LED headlights", "Virtual Cockpit with RS graphics", "Red-stitched Alcantara sports seats", "VAQ front differential lock", "640L boot capacity"],
                        "notes": "0-100km/h in 6.7s. Benchmark everyday enthusiast car."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Octavia RS Liftback / Combi",
                        "body_style": "5-door Combi wagon",
                        "engine_code": "DNPA",
                        "transmission": "7-speed DSG",
                        "drivetrain": "FWD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 53090,
                        "power_kw": 180,
                        "torque_nm": 370,
                        "fuel_l_100km": 6.8,
                        "towing_braked_kg": 1600,
                        "notes": "Current 180kW Octavia RS wagon with 640L luggage room."
                    }
                ]
            }
        ]
    },

    "peugeot/205-308-gti": {
        "make_slug": "peugeot",
        "model_slug": "205-308-gti",
        "name": "205, 306, 208 & 308 GTi",
        "vehicle_type": "Hot Hatchback",
        "segment": "Light / Small Performance Car",
        "years_sold_au": {"start": 1987, "end": 2020},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The aristocrats of French hot hatch engineering. For more than three decades in Australia, Peugeot's GTi lineage defined what a front-wheel drive performance car could achieve. From the featherweight, razor-sharp 205 GTi 1.9 that reset international benchmarks, through the passive rear-steering 306 GTi-6 with its class-first six-speed manual, to the Peugeot Sport-engineered 308 GTi 270 with Torsen LSD and massive Alcon brakes.",
        "australian_market_notes": "The 205 GTi arrived in Australia in October 1987. Despite strict Australian design rules mandating lower compression for unleaded fuel, its pure 880kg chassis, communicative unassisted steering, and adjustability on throttle lift-off won instant acclaim. The 306 GTi-6 followed in 1997, and the 208/308 GTi by Peugeot Sport concluded a golden era in 2020.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "205 GTi",
                "generation_name": "Peugeot 205 GTi 1.9",
                "years": {"start": 1987, "end": 1994},
                "body_styles": ["3-door hatchback"],
                "platform": "Peugeot 205",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Universally heralded as one of the purest hot hatches ever created. Weighing just 880kg with all-independent trailing-arm rear suspension, 15-inch Speedline alloys, and an eager 1.9L all-alloy engine.",
                "engines": [
                    {
                        "engine_code": "XU9JA/DKZ",
                        "name": "1.9L SOHC 8V Petrol (XU9)",
                        "displacement_cc": 1905,
                        "displacement_litres": 1.9,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 75,
                        "power_rpm": "6000",
                        "torque_nm": 142,
                        "torque_rpm": "3000",
                        "compression_ratio": "8.4:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "ADR catalytic converter tune (75kW-88kW in Australian delivery)."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "205 GTi 1.9",
                        "years": {"start": 1987, "end": 1994},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 29500,
                        "msrp_aud_max": 33990,
                        "fuel_consumption_l_100km": 7.8,
                        "kerb_weight_kg": 880,
                        "standard_features": ["15-inch Speedline 'pepper-pot' alloys", "Red carpet and red dash accents", "Half-leather sport seats", "Four-wheel disc brakes"],
                        "notes": "The holy grail hot hatch in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "205 GTi 1.9",
                        "body_style": "3-door hatchback",
                        "engine_code": "XU9JA/DKZ",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1987,
                        "years_end": 1994,
                        "msrp_aud": 31500,
                        "power_kw": 75,
                        "torque_nm": 142,
                        "fuel_l_100km": 7.8,
                        "towing_braked_kg": 750,
                        "notes": "Featherweight 880kg hot hatch benchmark."
                    }
                ]
            },
            {
                "series_code": "306 GTi-6",
                "generation_name": "Peugeot 306 S16 & GTi-6",
                "years": {"start": 1994, "end": 2001},
                "body_styles": ["3-door hatchback"],
                "platform": "Peugeot 306",
                "ancap_rating": "3 stars",
                "summary": "Pininfarina-styled masterpiece featuring a high-revving 120kW 2.0L 16V engine, passive rear-wheel steering rear axle, and the first close-ratio 6-speed manual gearbox fitted to a mass-production hot hatch.",
                "engines": [
                    {
                        "engine_code": "XU10J4RS",
                        "name": "2.0L DOHC 16V Petrol",
                        "displacement_cc": 1998,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 120,
                        "power_rpm": "6500",
                        "torque_nm": 193,
                        "torque_rpm": "5500",
                        "compression_ratio": "10.8:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "High-lift camshafts, tuned 4-2-1 stainless exhaust manifold; 7200rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "306 GTi-6",
                        "years": {"start": 1997, "end": 2001},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 38990,
                        "msrp_aud_max": 41990,
                        "fuel_consumption_l_100km": 8.9,
                        "kerb_weight_kg": 1215,
                        "standard_features": ["15-inch 'Cyclone' alloy wheels", "Close-ratio 6-speed gearbox", "Alcantara/leather sport seats", "Rear roof spoiler", "Rain sensing wipers"],
                        "notes": "0-100km/h in 7.9s. Revered for telepathic chassis response."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "306 GTi-6",
                        "body_style": "3-door hatchback",
                        "engine_code": "XU10J4RS",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1997,
                        "years_end": 2001,
                        "msrp_aud": 39990,
                        "power_kw": 120,
                        "torque_nm": 193,
                        "fuel_l_100km": 8.9,
                        "towing_braked_kg": 1000,
                        "notes": "First 6-speed manual hot hatch in Australia."
                    }
                ]
            },
            {
                "series_code": "308 GTi",
                "generation_name": "Peugeot 308 GTi by Peugeot Sport (250 & 270)",
                "years": {"start": 2016, "end": 2020},
                "body_styles": ["5-door hatchback"],
                "platform": "PSA EMP2",
                "ancap_rating": "5 stars",
                "summary": "Engineered directly by Peugeot Sport. Ultra-lightweight 1,205kg EMP2 platform, 1.6L THP engine developing up to 200kW (270hp), mechanical Torsen limited-slip differential, and massive Alcon 380mm four-piston front brakes.",
                "engines": [
                    {
                        "engine_code": "EP6FDTR",
                        "name": "1.6L THP 270 Turbo Petrol",
                        "displacement_cc": 1598,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 200,
                        "power_rpm": "6000",
                        "torque_nm": 330,
                        "torque_rpm": "1900-5000",
                        "compression_ratio": "9.2:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Mahle forged pistons, twin-scroll turbocharger with 2.5 bar boost pressure."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "308 GTi 270 by Peugeot Sport",
                        "years": {"start": 2016, "end": 2020},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 49990,
                        "msrp_aud_max": 51990,
                        "fuel_consumption_l_100km": 6.0,
                        "kerb_weight_kg": 1205,
                        "standard_features": ["Torsen mechanical limited-slip differential", "Alcon 380mm front discs with 4-piston calipers", "19-inch 'Carbone' reverse-drop alloys", "Peugeot Sport bucket seats with red stitching", "Coupe Franche two-tone paint option"],
                        "notes": "0-100km/h in 6.0s. Feathery 1205kg lightweight giant killer."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "308 GTi 270 by Peugeot Sport",
                        "body_style": "5-door hatchback",
                        "engine_code": "EP6FDTR",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2016,
                        "years_end": 2020,
                        "msrp_aud": 49990,
                        "power_kw": 200,
                        "torque_nm": 330,
                        "fuel_l_100km": 6.0,
                        "towing_braked_kg": 1200,
                        "notes": "200kW mechanical LSD track hero."
                    }
                ]
            }
        ]
    },

    "renault/clio-megane-rs": {
        "make_slug": "renault",
        "model_slug": "clio-megane-rs",
        "name": "Clio RS & Megane RS (Renault Sport)",
        "vehicle_type": "Hot Hatchback",
        "segment": "Light / Small Performance Car",
        "years_sold_au": {"start": 2001, "end": 2023},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The front-wheel-drive Nurburgring lap record conquerors. Developed by the wizards of Renault Sport at Dieppe, the Clio RS and Megane RS established an unbeatable pedigree in Australia for pure driving dynamics, PerfoHub independent steering axis suspension, mechanical limited-slip differentials, and Brembo stopping power.",
        "australian_market_notes": "First arrived in 2001 with the Clio RS 172. Australia quickly developed an obsessive relationship with Renault Sport, ranking second in the entire world outside Europe for Megane RS sales per capita. The Megane RS 265, 275 Trophy-R, and RS 300 Trophy repeatedly broke Australian production car front-wheel drive lap records.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Clio RS Gen 2 & 3",
                "generation_name": "Clio Renault Sport (RS 172 / 182 / 197 / 200)",
                "years": {"start": 2001, "end": 2013},
                "body_styles": ["3-door hatchback"],
                "platform": "Renault Clio II & III",
                "ancap_rating": "4 stars",
                "summary": "Naturally aspirated screaming 2.0L F4R engine revving past 7,000rpm. Progressed from the raw 124kW Clio 172 and 182 Cup to the wide-body Clio 197 and 200 with front PerfoHub double-axis struts, Brembo brakes, and functional rear aerodynamic diffuser.",
                "engines": [
                    {
                        "engine_code": "F4R-830",
                        "name": "2.0L 16V Naturally Aspirated Petrol (Clio 200)",
                        "displacement_cc": 1998,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 147,
                        "power_rpm": "7100",
                        "torque_nm": 215,
                        "torque_rpm": "5400",
                        "compression_ratio": "11.5:1",
                        "valvetrain": "DOHC 16-valve with VVT",
                        "notes": "Dieppe-built naturally aspirated jewel; 7500rpm rev limit with shift light."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Clio RS 182 Cup",
                        "years": {"start": 2004, "end": 2006},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 32990,
                        "msrp_aud_max": 34990,
                        "fuel_consumption_l_100km": 8.1,
                        "kerb_weight_kg": 1090,
                        "standard_features": ["16-inch anthracite alloys", "Twin center-exit exhausts", "Cup sports chassis (lower/stiffer)", "Cruise control"],
                        "notes": "Lightweight 1090kg pure hot hatch."
                    },
                    {
                        "badge_name": "Clio RS 200 Cup / Trophee",
                        "years": {"start": 2009, "end": 2013},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 36490,
                        "msrp_aud_max": 38990,
                        "fuel_consumption_l_100km": 8.2,
                        "kerb_weight_kg": 1204,
                        "standard_features": ["Brembo 4-piston front brakes", "PerfoHub front suspension", "Functional rear diffuser", "Recaro bucket seats option", "Liquid Yellow hero paint"],
                        "notes": "The apex of naturally aspirated hot hatch chassis tuning."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Clio RS 200 Cup / Trophee",
                        "body_style": "3-door hatchback",
                        "engine_code": "F4R-830",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2009,
                        "years_end": 2013,
                        "msrp_aud": 36990,
                        "power_kw": 147,
                        "torque_nm": 215,
                        "fuel_l_100km": 8.2,
                        "towing_braked_kg": 0,
                        "notes": "7100rpm naturally aspirated Dieppe-tuned track star."
                    }
                ]
            },
            {
                "series_code": "Megane RS Gen 3",
                "generation_name": "Megane RS 250, 265 & 275 Trophy (Megane III)",
                "years": {"start": 2010, "end": 2017},
                "body_styles": ["3-door coupe"],
                "platform": "Renault Megane III Coupe",
                "ancap_rating": "5 stars",
                "summary": "Widely acknowledged as the greatest front-wheel drive track car of its decade. Armed with PerfoHub suspension eliminating torque steer, mechanical mechanical limited-slip differential, Brembo brakes, 2.0L turbo (184kW to 201kW), and record-smashing 275 Trophy-R.",
                "engines": [
                    {
                        "engine_code": "F4Rt",
                        "name": "2.0L 16V Turbo Petrol (RS 265 / 275)",
                        "displacement_cc": 1998,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 201,
                        "power_rpm": "5500",
                        "torque_nm": 360,
                        "torque_rpm": "3000-5000",
                        "compression_ratio": "8.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Twin-scroll turbocharger with RS Monitor telemetry system."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Megane RS 265 Cup / Trophy+",
                        "years": {"start": 2012, "end": 2016},
                        "body_styles": ["3-door coupe"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 42640,
                        "msrp_aud_max": 51640,
                        "fuel_consumption_l_100km": 8.2,
                        "kerb_weight_kg": 1374,
                        "standard_features": ["Mechanical mechanical limited-slip differential", "Brembo 4-piston calipers in red", "19-inch Steev alloy wheels", "Recaro leather bucket seats", "RS Monitor telemetry"],
                        "notes": "Australia was the #1 Megane RS market per capita in the world."
                    },
                    {
                        "badge_name": "Megane RS 275 Trophy-R",
                        "years": {"start": 2014, "end": 2015},
                        "body_styles": ["3-door coupe"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 61990,
                        "msrp_aud_max": 64990,
                        "fuel_consumption_l_100km": 7.5,
                        "kerb_weight_kg": 1280,
                        "standard_features": ["Ohlins Road & Track adjustable dampers", "Akrapovic titanium exhaust system", "Recaro Pole Position composite seats", "Rear seat delete with harness bar", "Michelin Pilot Sport Cup 2 tyres"],
                        "notes": "0-100km/h in 5.8s. Nurburgring FWD lap record holder (7m54.36s). Only 50 units imported to Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Megane RS 265 Cup / Trophy+",
                        "body_style": "3-door coupe",
                        "engine_code": "F4Rt",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2012,
                        "years_end": 2016,
                        "msrp_aud": 45990,
                        "power_kw": 195,
                        "torque_nm": 360,
                        "fuel_l_100km": 8.2,
                        "towing_braked_kg": 0,
                        "notes": "Benchmark front-wheel drive mechanical LSD track coupe."
                    }
                ]
            },
            {
                "series_code": "Megane RS Gen 4",
                "generation_name": "Megane RS 280 & RS 300 Trophy (Megane IV)",
                "years": {"start": 2018, "end": 2023},
                "body_styles": ["5-door hatchback"],
                "platform": "Renault CMF-CD",
                "ancap_rating": "5 stars",
                "summary": "5-door practicality equipped with class-exclusive 4Control four-wheel steering, hydraulic compression bump stops, 1.8L Alpine A110-derived turbo engine, and RS 300 Trophy delivering 221kW and 420Nm.",
                "engines": [
                    {
                        "engine_code": "M5Pt",
                        "name": "1.8L Turbo Petrol (RS 300 Trophy)",
                        "displacement_cc": 1798,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 221,
                        "power_rpm": "6000",
                        "torque_nm": 420,
                        "torque_rpm": "3200-4800",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Ceramic ball-bearing turbocharger derived from Renault F1 technology."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Megane RS 300 Trophy",
                        "years": {"start": 2019, "end": 2023},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "6-speed EDC dual-clutch"],
                        "msrp_aud_min": 53990,
                        "msrp_aud_max": 62990,
                        "fuel_consumption_l_100km": 8.0,
                        "kerb_weight_kg": 1419,
                        "standard_features": ["4Control four-wheel steering", "Torsen mechanical LSD", "Bi-material Brembo front brake discs", "19-inch 'Jerez' alloy wheels", "Active mechanical exhaust valve"],
                        "notes": "0-100km/h in 5.7s. Final petrol Renault Sport model."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Megane RS 300 Trophy",
                        "body_style": "5-door hatchback",
                        "engine_code": "M5Pt",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2019,
                        "years_end": 2023,
                        "msrp_aud": 56990,
                        "power_kw": 221,
                        "torque_nm": 400,
                        "fuel_l_100km": 8.0,
                        "towing_braked_kg": 0,
                        "notes": "221kW 4Control four-wheel steer hot hatch."
                    }
                ]
            }
        ]
    }
}
