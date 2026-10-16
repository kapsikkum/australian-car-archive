"""
Wave 2 Deep-Dive Models Part 1 (Models 1 to 8):
1. volkswagen/beetle-kombi
2. volkswagen/tiguan
3. volkswagen/polo
4. bmw/5-series-m5
5. bmw/x5
6. mercedes-benz/e-class
7. mercedes-benz/g-class
8. audi/a3-s3-rs3
"""
from typing import Dict, Any

WAVE2_MODELS_PART1: Dict[str, Dict[str, Any]] = {
    "volkswagen/beetle-kombi": {
        "make_slug": "volkswagen",
        "model_slug": "beetle-kombi",
        "name": "Beetle, Kombi & Country Buggy",
        "vehicle_type": "Sedan / Convertible / Microbus / Van / Ute / Off-Roader",
        "segment": "Classic Compact / Light Commercial",
        "years_sold_au": {"start": 1954, "end": 1979},
        "locally_built": True,
        "assembly_plants_au": ["Clayton, Victoria (1954-1976)"],
        "overview": "The bedrock of Volkswagen's Australian history. Starting with CKD assembly in Melbourne in 1954, the Type 1 Beetle and Type 2 Kombi progressed to full local manufacture at Clayton, Victoria, achieving over 80% Australian domestic content. Clayton also designed and manufactured the unique Australian Volkswagen Country Buggy (Type 197).",
        "australian_market_notes": "First assembled at Martin & King in Clayton in 1954 before Volkswagen Australasia purchased the plant. The Beetle became Australia's top-selling small car through the 1960s, while the Kombi became an indelible part of Australian surf culture, commercial trades, and camper touring. Clayton produced 1,956 Australian-exclusive Country Buggies in 1968.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Type 1",
                "generation_name": "Beetle Type 1 (Sedan & Super Beetle)",
                "years": {"start": 1954, "end": 1976},
                "body_styles": ["2-door sedan", "2-door cabriolet"],
                "platform": "Volkswagen Type 1",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Clayton-assembled air-cooled rear-engine legend. Progressed from 1192cc 1200 through 1285cc 1300, 1493cc 1500, to 1584cc 1600 Super Beetle (1302S and 1303S) with MacPherson strut front suspension.",
                "engines": [
                    {
                        "engine_code": "1200",
                        "name": "1.2L Air-Cooled Flat-4",
                        "displacement_cc": 1192,
                        "displacement_litres": 1.2,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 25,
                        "power_rpm": "3400",
                        "torque_nm": 82,
                        "torque_rpm": "2000",
                        "compression_ratio": "6.6:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Single Solex downdraft carburettor, 6-volt electrical system on early models."
                    },
                    {
                        "engine_code": "1300",
                        "name": "1.3L Air-Cooled Flat-4",
                        "displacement_cc": 1285,
                        "displacement_litres": 1.3,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 29,
                        "power_rpm": "4100",
                        "torque_nm": 87,
                        "torque_rpm": "2600",
                        "compression_ratio": "7.3:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Introduced in 1966 with slotted wheels and upgraded brakes."
                    },
                    {
                        "engine_code": "1500",
                        "name": "1.5L Air-Cooled Flat-4",
                        "displacement_cc": 1493,
                        "displacement_litres": 1.5,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 33,
                        "power_rpm": "4200",
                        "torque_nm": 106,
                        "torque_rpm": "2600",
                        "compression_ratio": "7.5:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Standard front disc brakes on Australian delivered 1500 Beetles from 1967."
                    },
                    {
                        "engine_code": "1600",
                        "name": "1.6L Air-Cooled Flat-4 Twin-Port",
                        "displacement_cc": 1584,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 37,
                        "power_rpm": "4400",
                        "torque_nm": 106,
                        "torque_rpm": "3000",
                        "compression_ratio": "7.5:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Twin-port cylinder heads, fitted to Super Beetle 1302S and 1303S."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Standard 1200",
                        "years": {"start": 1954, "end": 1965},
                        "body_styles": ["2-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 1798,
                        "msrp_aud_max": 2040,
                        "fuel_consumption_l_100km": 7.5,
                        "kerb_weight_kg": 730,
                        "standard_features": ["Vinyl seating", "Spare wheel under front hood", "Torsion bar suspension"],
                        "notes": "The foundation car that established Volkswagen throughout regional and urban Australia."
                    },
                    {
                        "badge_name": "Deluxe 1300",
                        "years": {"start": 1966, "end": 1970},
                        "body_styles": ["2-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 1990,
                        "msrp_aud_max": 2250,
                        "fuel_consumption_l_100km": 7.8,
                        "kerb_weight_kg": 780,
                        "standard_features": ["Chrome bumpers", "Ventilated wheels", "Push-button door handles", "Padded dash"],
                        "notes": "Major Australian volume seller built in Melbourne."
                    },
                    {
                        "badge_name": "Super Beetle 1302S / 1303S",
                        "years": {"start": 1971, "end": 1976},
                        "body_styles": ["2-door sedan", "2-door cabriolet"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual", "3-speed Semi-Automatic"],
                        "msrp_aud_min": 2565,
                        "msrp_aud_max": 3290,
                        "fuel_consumption_l_100km": 8.4,
                        "kerb_weight_kg": 870,
                        "standard_features": ["MacPherson front struts", "Curved windscreen (1303)", "Bigger boot space", "1600 engine"],
                        "notes": "Final evolution of the Clayton-assembled Beetle."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Standard 1200",
                        "body_style": "2-door sedan",
                        "engine_code": "1200",
                        "transmission": "4-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1954,
                        "years_end": 1965,
                        "msrp_aud": 1850,
                        "power_kw": 25,
                        "torque_nm": 82,
                        "fuel_l_100km": 7.5,
                        "towing_braked_kg": 400,
                        "notes": "Clayton CKD / full manufacture specification."
                    },
                    {
                        "badge_name": "Super Beetle 1302S / 1303S",
                        "body_style": "2-door sedan",
                        "engine_code": "1600",
                        "transmission": "4-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1971,
                        "years_end": 1976,
                        "msrp_aud": 2795,
                        "power_kw": 37,
                        "torque_nm": 106,
                        "fuel_l_100km": 8.4,
                        "towing_braked_kg": 500,
                        "notes": "Independent rear suspension and MacPherson strut front."
                    }
                ]
            },
            {
                "series_code": "Type 197",
                "generation_name": "Country Buggy (Type 197)",
                "years": {"start": 1968, "end": 1969},
                "body_styles": ["2-door open utility / roadster"],
                "platform": "Modified Type 1 chassis with Type 2 reduction hubs",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Designed, engineered and manufactured exclusively in Australia by Volkswagen Australasia at Clayton, Victoria under project director Rudi Herz. Built using Beetle floorpans, Transporter reduction-gear portal hubs, and folded sheet-metal bodywork for extreme ground clearance in the Australian outback.",
                "engines": [
                    {
                        "engine_code": "1300",
                        "name": "1.3L Air-Cooled Flat-4",
                        "displacement_cc": 1285,
                        "displacement_litres": 1.3,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 29,
                        "power_rpm": "4100",
                        "torque_nm": 87,
                        "torque_rpm": "2600",
                        "compression_ratio": "7.3:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Robust air-cooled engine with heavy-duty oil-bath air cleaner for bulldust."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Country Buggy",
                        "years": {"start": 1968, "end": 1969},
                        "body_styles": ["2-door open utility / roadster"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual with reduction hubs"],
                        "msrp_aud_min": 1598,
                        "msrp_aud_max": 1820,
                        "fuel_consumption_l_100km": 8.9,
                        "kerb_weight_kg": 760,
                        "standard_features": ["Canvas soft-top", "Folding windshield", "High ground clearance (230mm)", "Rear cargo tray"],
                        "notes": "1,956 units built at Clayton. Highly prized Australian collector's icon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Country Buggy",
                        "body_style": "2-door open utility / roadster",
                        "engine_code": "1300",
                        "transmission": "4-speed manual with reduction hubs",
                        "drivetrain": "RWD",
                        "years_start": 1968,
                        "years_end": 1969,
                        "msrp_aud": 1695,
                        "power_kw": 29,
                        "torque_nm": 87,
                        "fuel_l_100km": 8.9,
                        "towing_braked_kg": 400,
                        "notes": "Australian engineered Type 197 open off-road utility."
                    }
                ]
            },
            {
                "series_code": "Type 2",
                "generation_name": "Kombi / Microbus / Transporter (Type 2 T1 & T2)",
                "years": {"start": 1954, "end": 1979},
                "body_styles": ["Van", "Microbus", "Dual-cab ute", "Single-cab ute", "Campmobile"],
                "platform": "Volkswagen Type 2",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The beloved Australian Kombi across Split-screen (T1) and Bay-window (T2) generations. Clayton-assembled with local interior camper fit-outs, dual-cab work utes, and delivery vans.",
                "engines": [
                    {
                        "engine_code": "1600-T2",
                        "name": "1.6L Air-Cooled Flat-4",
                        "displacement_cc": 1584,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 37,
                        "power_rpm": "4000",
                        "torque_nm": 106,
                        "torque_rpm": "2800",
                        "compression_ratio": "7.5:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Standard power unit on late Split and early Bay window Kombis."
                    },
                    {
                        "engine_code": "2.0-Type4",
                        "name": "2.0L Air-Cooled Flat-4 Twin-Carb",
                        "displacement_cc": 1970,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Flat-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 52,
                        "power_rpm": "4200",
                        "torque_nm": 143,
                        "torque_rpm": "2800",
                        "compression_ratio": "7.3:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Type 4 pancake engine with twin Solex carburettors for Australian highway touring."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Transporter Van / Ute",
                        "years": {"start": 1954, "end": 1979},
                        "body_styles": ["Van", "Single-cab ute", "Dual-cab ute"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 2150,
                        "msrp_aud_max": 4200,
                        "fuel_consumption_l_100km": 10.5,
                        "kerb_weight_kg": 1180,
                        "standard_features": ["Flat cargo floor", "Drop-side ute gates", "Sliding side cargo door (T2)"],
                        "notes": "Clayton-assembled commercial workhorse."
                    },
                    {
                        "badge_name": "Microbus Deluxe & Campmobile",
                        "years": {"start": 1955, "end": 1979},
                        "body_styles": ["Microbus", "Campmobile"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual", "3-speed automatic"],
                        "msrp_aud_min": 2690,
                        "msrp_aud_max": 5990,
                        "fuel_consumption_l_100km": 11.2,
                        "kerb_weight_kg": 1340,
                        "standard_features": ["8-seater / 9-seater seating", "Pop-top camper roof option", "Twin beds", "Sink and icebox"],
                        "notes": "Icon of Australian surfing and camping holidays."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Microbus Deluxe & Campmobile",
                        "body_style": "Campmobile",
                        "engine_code": "2.0-Type4",
                        "transmission": "4-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1976,
                        "years_end": 1979,
                        "msrp_aud": 5690,
                        "power_kw": 52,
                        "torque_nm": 143,
                        "fuel_l_100km": 11.2,
                        "towing_braked_kg": 1000,
                        "notes": "Peak Australian specification Bay-window camper with 2.0L twin-carb engine."
                    }
                ]
            }
        ]
    },

    "volkswagen/tiguan": {
        "make_slug": "volkswagen",
        "model_slug": "tiguan",
        "name": "Tiguan",
        "vehicle_type": "Medium SUV",
        "segment": "Medium SUV",
        "years_sold_au": {"start": 2008, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Volkswagen's powerhouse medium SUV in Australia, delivering European road manners, turbocharged TSI petrol and TDI diesel powertrains, 4Motion all-wheel drive, spacious 5-seat and 7-seat Allspace layouts, and the blisteringly fast 235kW Tiguan R.",
        "australian_market_notes": "Introduced to Australia in May 2008 on the PQ35 platform. The second-generation MQB Tiguan arrived in 2016 and became a runaway hit with Australian family buyers, particularly the Golf GTI-engined 162TSI Highline/R-Line and the 235kW Tiguan R launched in 2022.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "5N",
                "generation_name": "Tiguan First Generation (Typ 5N)",
                "years": {"start": 2008, "end": 2016},
                "body_styles": ["5-door SUV"],
                "platform": "Volkswagen Group PQ35",
                "ancap_rating": "5 stars",
                "summary": "First-gen compact/medium SUV with 4Motion Haldex AWD. Engines included 2.0 TDI (103kW), 2.0 TSI (125TSI, 132TSI, and 155TSI R-Line from Golf GTI).",
                "engines": [
                    {
                        "engine_code": "CAWA",
                        "name": "2.0L TSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 125,
                        "power_rpm": "4300",
                        "torque_nm": 280,
                        "torque_rpm": "1700-4200",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 Gen 1 turbo petrol engine."
                    },
                    {
                        "engine_code": "CCZB",
                        "name": "2.0L TSI 155TSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 155,
                        "power_rpm": "5300",
                        "torque_nm": 280,
                        "torque_rpm": "1700-5200",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Golf GTI Mk6 powertrain in 155TSI R-Line."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "125TSI / 132TSI Pacific",
                        "years": {"start": 2008, "end": 2016},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual", "7-speed DSG"],
                        "msrp_aud_min": 33990,
                        "msrp_aud_max": 41990,
                        "fuel_consumption_l_100km": 8.8,
                        "kerb_weight_kg": 1630,
                        "standard_features": ["16-inch alloy wheels", "Dual-zone climate control", "4Motion AWD", "Roof rails"],
                        "notes": "Core Australian family specification."
                    },
                    {
                        "badge_name": "155TSI R-Line",
                        "years": {"start": 2013, "end": 2016},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 44990,
                        "msrp_aud_max": 48990,
                        "fuel_consumption_l_100km": 8.7,
                        "kerb_weight_kg": 1660,
                        "standard_features": ["18-inch Mallory alloys", "R-Line body kit", "Sports suspension", "Vienna leather upholstery"],
                        "notes": "Performance flagship of the 5N range."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "155TSI R-Line",
                        "body_style": "5-door SUV",
                        "engine_code": "CCZB",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2013,
                        "years_end": 2016,
                        "msrp_aud": 46990,
                        "power_kw": 155,
                        "torque_nm": 280,
                        "fuel_l_100km": 8.7,
                        "towing_braked_kg": 2000,
                        "notes": "Top-tier 5N Tiguan with Golf GTI power."
                    }
                ]
            },
            {
                "series_code": "AD/BW",
                "generation_name": "Tiguan Second Generation & Allspace (Typ AD/BW)",
                "years": {"start": 2016, "end": 2023},
                "body_styles": ["5-door SUV", "7-seat SUV (Allspace)"],
                "platform": "Volkswagen Group MQB",
                "ancap_rating": "5 stars",
                "summary": "Transformative MQB second generation; available in 5-seat and extended 7-seat Allspace bodies. Highlighted by the hugely popular 162TSI Highline/R-Line (EA888 162kW) and the halo Tiguan R with 235kW, 4Motion torque vectoring, and Akrapovic exhaust.",
                "engines": [
                    {
                        "engine_code": "CHHB",
                        "name": "2.0L TSI 162TSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 162,
                        "power_rpm": "4500-6200",
                        "torque_nm": 350,
                        "torque_rpm": "1500-4400",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Golf GTI engine tuned for AWD Tiguan; accounted for majority of AU Tiguan sales."
                    },
                    {
                        "engine_code": "DNF",
                        "name": "2.0L TSI Tiguan R Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 235,
                        "power_rpm": "5200-6600",
                        "torque_nm": 400,
                        "torque_rpm": "2100-5350",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 evo4 shared with Golf 8 R, with R-Performance Torque Vectoring."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "162TSI Highline / R-Line",
                        "years": {"start": 2016, "end": 2023},
                        "body_styles": ["5-door SUV", "7-seat SUV (Allspace)"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 48490,
                        "msrp_aud_max": 59990,
                        "fuel_consumption_l_100km": 8.1,
                        "kerb_weight_kg": 1695,
                        "standard_features": ["Digital Cockpit", "9.2-inch Discover Pro nav", "Adaptive Chassis Control", "Vienna leather", "20-inch Suzuka alloys"],
                        "notes": "Australia's favorite performance family SUV."
                    },
                    {
                        "badge_name": "Tiguan R",
                        "years": {"start": 2022, "end": 2023},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 68990,
                        "msrp_aud_max": 73790,
                        "fuel_consumption_l_100km": 8.8,
                        "kerb_weight_kg": 1740,
                        "standard_features": ["21-inch Estoril alloys", "Blue Nappa leather R seats", "Torque Vectoring rear differential", "Matrix LED headlights", "R front bumper with large air intakes"],
                        "notes": "0-100km/h in 4.9 seconds. Cult performance hit."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "162TSI Highline / R-Line",
                        "body_style": "5-door SUV",
                        "engine_code": "CHHB",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2016,
                        "years_end": 2023,
                        "msrp_aud": 54990,
                        "power_kw": 162,
                        "torque_nm": 350,
                        "fuel_l_100km": 8.1,
                        "towing_braked_kg": 2500,
                        "notes": "Benchmark family SUV with 2500kg towing capacity."
                    },
                    {
                        "badge_name": "Tiguan R",
                        "body_style": "5-door SUV",
                        "engine_code": "DNF",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2022,
                        "years_end": 2023,
                        "msrp_aud": 70990,
                        "power_kw": 235,
                        "torque_nm": 400,
                        "fuel_l_100km": 8.8,
                        "towing_braked_kg": 2200,
                        "notes": "235kW hyper-SUV sprint champion."
                    }
                ]
            },
            {
                "series_code": "CT",
                "generation_name": "Tiguan Third Generation (Typ CT)",
                "years": {"start": 2024, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "Volkswagen Group MQB evo",
                "ancap_rating": "5 stars",
                "summary": "Third-generation Tiguan built on MQB evo with aerodynamic drag reduction (Cd 0.28), massive 15-inch central touchscreen, rotary driving experience dial, and high-output 195TSI R-Line powertrain.",
                "engines": [
                    {
                        "engine_code": "EA888-evo4-195",
                        "name": "2.0L TSI 195TSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 195,
                        "power_rpm": "5000-6500",
                        "torque_nm": 400,
                        "torque_rpm": "1600-4300",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Direct-injected 195kW EA888 evo4 petrol turbo."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "195TSI R-Line",
                        "years": {"start": 2024, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 62990,
                        "msrp_aud_max": 68990,
                        "fuel_consumption_l_100km": 7.9,
                        "kerb_weight_kg": 1720,
                        "standard_features": ["15-inch MIB4 infotainment", "DCC Pro twin-valve dampers", "IQ.LIGHT HD Matrix LEDs", "HUD"],
                        "notes": "New-generation technology flagship."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "195TSI R-Line",
                        "body_style": "5-door SUV",
                        "engine_code": "EA888-evo4-195",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2024,
                        "years_end": "Present",
                        "msrp_aud": 64990,
                        "power_kw": 195,
                        "torque_nm": 400,
                        "fuel_l_100km": 7.9,
                        "towing_braked_kg": 2300,
                        "notes": "Next-generation 195kW AWD Tiguan."
                    }
                ]
            }
        ]
    },

    "volkswagen/polo": {
        "make_slug": "volkswagen",
        "model_slug": "polo",
        "name": "Polo",
        "vehicle_type": "Hatchback",
        "segment": "Light Car",
        "years_sold_au": {"start": 1996, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Volkswagen's premium compact hatchback in Australia. Across four generations from the 6N to the modern MQB AW, the Polo brought big-car refinement, solid German safety, and pocket-rocket performance through the beloved Polo GTI.",
        "australian_market_notes": "First officially imported to Australia in 1996 with the 6N generation. The Polo GTI arrived in 2005 (9N3 1.8 20V Turbo), creating a loyal cult following among Australian driving enthusiasts that grew stronger through the twincharged 6R and 2.0-litre AW models.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "6N",
                "generation_name": "Polo Third Generation (Typ 6N/6N2)",
                "years": {"start": 1996, "end": 2002},
                "body_styles": ["3-door hatchback", "5-door hatchback"],
                "platform": "Volkswagen Group A03",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Introduced the Polo nameplate to Australia in 1996. Features included galvanized steel body panels, dual airbags, 1.6L 8V engine, and the distinctive Open Air sliding fabric roof.",
                "engines": [
                    {
                        "engine_code": "AEE",
                        "name": "1.6L SOHC Petrol",
                        "displacement_cc": 1598,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 55,
                        "power_rpm": "5200",
                        "torque_nm": 135,
                        "torque_rpm": "2800",
                        "compression_ratio": "9.8:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "Multipoint fuel injection with torquey low-end delivery."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Polo 1.6 / Open Air",
                        "years": {"start": 1996, "end": 2002},
                        "body_styles": ["3-door hatchback", "5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 17990,
                        "msrp_aud_max": 22990,
                        "fuel_consumption_l_100km": 7.4,
                        "kerb_weight_kg": 990,
                        "standard_features": ["Dual front airbags", "Power steering", "Immobiliser", "Full-length electric canvas roof (Open Air)"],
                        "notes": "Established the Polo as a premium light car in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Polo 1.6 / Open Air",
                        "body_style": "5-door hatchback",
                        "engine_code": "AEE",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1996,
                        "years_end": 2002,
                        "msrp_aud": 18990,
                        "power_kw": 55,
                        "torque_nm": 135,
                        "fuel_l_100km": 7.4,
                        "towing_braked_kg": 800,
                        "notes": "Australian launch specification."
                    }
                ]
            },
            {
                "series_code": "9N",
                "generation_name": "Polo Fourth Generation (Typ 9N/9N3)",
                "years": {"start": 2002, "end": 2010},
                "body_styles": ["3-door hatchback", "5-door hatchback"],
                "platform": "Volkswagen Group PQ24",
                "ancap_rating": "4 stars",
                "summary": "Recognizable by its distinctive twin round headlights (facelifted in 2005 to 9N3 single units). Spawned the first Australian Polo GTI in 2005, powered by the 110kW 1.8L 20V turbo.",
                "engines": [
                    {
                        "engine_code": "BJX",
                        "name": "1.8L 20V Turbo Petrol (GTI)",
                        "displacement_cc": 1781,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 110,
                        "power_rpm": "5800",
                        "torque_nm": 220,
                        "torque_rpm": "1950-4500",
                        "compression_ratio": "9.5:1",
                        "valvetrain": "DOHC 20-valve (5 valves per cylinder)",
                        "notes": "Legendary 20V turbo shared with Golf GTI Mk4 and Audi TT."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Polo GTI",
                        "years": {"start": 2005, "end": 2010},
                        "body_styles": ["3-door hatchback", "5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 26990,
                        "msrp_aud_max": 28990,
                        "fuel_consumption_l_100km": 7.8,
                        "kerb_weight_kg": 1160,
                        "standard_features": ["16-inch 'Denver' alloys", "Interlagos tartan cloth seats", "Honeycombed GTI grille", "Twin chrome exhaust tips"],
                        "notes": "Instant pocket-rocket sensation in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Polo GTI",
                        "body_style": "3-door hatchback",
                        "engine_code": "BJX",
                        "transmission": "5-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2005,
                        "years_end": 2010,
                        "msrp_aud": 26990,
                        "power_kw": 110,
                        "torque_nm": 220,
                        "fuel_l_100km": 7.8,
                        "towing_braked_kg": 1000,
                        "notes": "1.8 20V Turbo hot hatch."
                    }
                ]
            },
            {
                "series_code": "6R/6C",
                "generation_name": "Polo Fifth Generation (Typ 6R/6C)",
                "years": {"start": 2010, "end": 2018},
                "body_styles": ["3-door hatchback", "5-door hatchback"],
                "platform": "Volkswagen Group PQ25",
                "ancap_rating": "5 stars",
                "summary": "Won 2010 World Car of the Year. Featured 77TSI turbo petrol engines and the GTI with 1.4 TSI twincharged (supercharged and turbocharged, 132kW), followed in the 6C facelift by the 1.8 TSI (141kW) with manual and 7-speed DSG options.",
                "engines": [
                    {
                        "engine_code": "CAVE/CTHE",
                        "name": "1.4L TSI Twincharged Petrol",
                        "displacement_cc": 1390,
                        "displacement_litres": 1.4,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Twincharged (Supercharged & Turbocharged)",
                        "fuel_type": "Petrol",
                        "power_kw": 132,
                        "power_rpm": "6200",
                        "torque_nm": 250,
                        "torque_rpm": "2000-4500",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Roots-type supercharger for low end plus turbocharger for high end."
                    },
                    {
                        "engine_code": "DAJA",
                        "name": "1.8L TSI Turbo Petrol (6C)",
                        "displacement_cc": 1798,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 141,
                        "power_rpm": "5400-6200",
                        "torque_nm": 320,
                        "torque_rpm": "1450-4200",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 Gen 3 turbo petrol with 320Nm in 6-speed manual guise."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "77TSI Comfortline",
                        "years": {"start": 2010, "end": 2014},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "7-speed DSG"],
                        "msrp_aud_min": 19870,
                        "msrp_aud_max": 22370,
                        "fuel_consumption_l_100km": 5.5,
                        "kerb_weight_kg": 1110,
                        "standard_features": ["15-inch alloys", "Cruise control", "Touchscreen audio", "Hill start assist"],
                        "notes": "Australian Wheels Car of the Year finalist."
                    },
                    {
                        "badge_name": "Polo GTI",
                        "years": {"start": 2010, "end": 2018},
                        "body_styles": ["3-door hatchback", "5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "7-speed DSG"],
                        "msrp_aud_min": 27490,
                        "msrp_aud_max": 31990,
                        "fuel_consumption_l_100km": 6.1,
                        "kerb_weight_kg": 1189,
                        "standard_features": ["17-inch Monza alloys", "XDL electronic diff lock", "Clark tartan sport seats", "Red brake calipers"],
                        "notes": "0-100km/h in 6.7 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Polo GTI",
                        "body_style": "5-door hatchback",
                        "engine_code": "DAJA",
                        "transmission": "6-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 2015,
                        "years_end": 2018,
                        "msrp_aud": 27490,
                        "power_kw": 141,
                        "torque_nm": 320,
                        "fuel_l_100km": 6.0,
                        "towing_braked_kg": 1200,
                        "notes": "1.8 TSI manual 320Nm enthusiast specification."
                    }
                ]
            },
            {
                "series_code": "AW",
                "generation_name": "Polo Sixth Generation (Typ AW)",
                "years": {"start": 2018, "end": "Present"},
                "body_styles": ["5-door hatchback"],
                "platform": "Volkswagen Group MQB A0",
                "ancap_rating": "5 stars",
                "summary": "Built on the MQB A0 platform, offering Golf-sized interior room, 351-litre boot, Digital Cockpit, and the Polo GTI armed with a full 2.0-litre EA888 turbo engine producing 147kW/152kW.",
                "engines": [
                    {
                        "engine_code": "DKZC",
                        "name": "2.0L TSI 147TSI Turbo Petrol",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 147,
                        "power_rpm": "4400-6000",
                        "torque_nm": 320,
                        "torque_rpm": "1500-4400",
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "2.0-litre EA888 engine providing hot hatch supremacy."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "85TSI Style",
                        "years": {"start": 2018, "end": "Present"},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 25990,
                        "msrp_aud_max": 31490,
                        "fuel_consumption_l_100km": 5.4,
                        "kerb_weight_kg": 1175,
                        "standard_features": ["Digital Cockpit", "Wireless Apple CarPlay", "Front Assist AEB", "Lane Assist"],
                        "notes": "Premium light hatchback."
                    },
                    {
                        "badge_name": "Polo GTI",
                        "years": {"start": 2018, "end": "Present"},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed DSG", "7-speed DSG"],
                        "msrp_aud_min": 31990,
                        "msrp_aud_max": 40390,
                        "fuel_consumption_l_100km": 6.5,
                        "kerb_weight_kg": 1285,
                        "standard_features": ["18-inch Milton alloys", "Sport Select adaptive dampers", "Clark tartan sport seats", "Matrix LED headlights"],
                        "notes": "2.0L turbocharged flagship, 0-100km/h in 6.7 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Polo GTI",
                        "body_style": "5-door hatchback",
                        "engine_code": "DKZC",
                        "transmission": "6-speed DSG",
                        "drivetrain": "FWD",
                        "years_start": 2018,
                        "years_end": "Present",
                        "msrp_aud": 38790,
                        "power_kw": 147,
                        "torque_nm": 320,
                        "fuel_l_100km": 6.5,
                        "towing_braked_kg": 1200,
                        "notes": "2.0 TSI hot hatch with adaptive damping."
                    }
                ]
            }
        ]
    },

    "bmw/5-series-m5": {
        "make_slug": "bmw",
        "model_slug": "5-series-m5",
        "name": "5 Series & M5",
        "vehicle_type": "Sedan / Touring Wagon",
        "segment": "Large Luxury Executive Sedan",
        "years_sold_au": {"start": 1973, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The definitive executive express in Australia across eight generations. The 5 Series established BMW's benchmark rear-wheel-drive chassis dynamics, silky inline-sixes, and thunderous V8s, culminating in the peerless BMW M5 from the high-revving S38, naturally aspirated V8 S62, screaming V10 S85, to the twin-turbo V8 M xDrive M5 Competition.",
        "australian_market_notes": "First sold in Australia in 1973 with the E12 520. Frank Gardner and Allan Grice famously raced the E12 and E28 in the Australian Touring Car Championship. The E39 M5 and E60 V10 M5 hold revered places in Australian motoring folklore, with Australia consistently ranking in the top five per-capita markets for M5 sales globally.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "E28",
                "generation_name": "5 Series E28 & M535i",
                "years": {"start": 1981, "end": 1988},
                "body_styles": ["4-door sedan"],
                "platform": "BMW E28",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The shark-nose executive sports sedan; 520i, 528i, and halo M535i engineered by BMW Motorsport with 3.4L M30 big-six, M-Technic suspension, and limited-slip differential.",
                "engines": [
                    {
                        "engine_code": "M30B34",
                        "name": "3.4L SOHC Inline-6",
                        "displacement_cc": 3430,
                        "displacement_litres": 3.4,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 136,
                        "power_rpm": "5400",
                        "torque_nm": 290,
                        "torque_rpm": "4000",
                        "compression_ratio": "8.0:1",
                        "valvetrain": "SOHC 12-valve",
                        "notes": "ADR unleaded specification with Bosch Motronic injection."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "M535i",
                        "years": {"start": 1985, "end": 1988},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual (dogleg)", "4-speed automatic"],
                        "msrp_aud_min": 64500,
                        "msrp_aud_max": 76900,
                        "fuel_consumption_l_100km": 11.5,
                        "kerb_weight_kg": 1390,
                        "standard_features": ["M Technic bodykit", "Bilstein sports dampers", "25% LSD", "Recaro sports seats"],
                        "notes": "Precursor to full Australian M5 delivery."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M535i",
                        "body_style": "4-door sedan",
                        "engine_code": "M30B34",
                        "transmission": "5-speed manual (dogleg)",
                        "drivetrain": "RWD",
                        "years_start": 1985,
                        "years_end": 1988,
                        "msrp_aud": 69900,
                        "power_kw": 136,
                        "torque_nm": 290,
                        "fuel_l_100km": 11.5,
                        "towing_braked_kg": 1400,
                        "notes": "Australian delivery M-Technic sports sedan."
                    }
                ]
            },
            {
                "series_code": "E34",
                "generation_name": "5 Series E34 & M5",
                "years": {"start": 1988, "end": 1996},
                "body_styles": ["4-door sedan", "Touring wagon"],
                "platform": "BMW E34",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Classic Claus Luthe design. Featured multi-link rear suspension, 24V M50 sixes, the muscular 540i 4.0L V8, and the hand-built S38-powered BMW M5.",
                "engines": [
                    {
                        "engine_code": "M60B40",
                        "name": "4.0L 32V DOHC V8",
                        "displacement_cc": 3982,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 210,
                        "power_rpm": "5800",
                        "torque_nm": 400,
                        "torque_rpm": "4500",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "All-aluminium V8, 5-speed automatic or 6-speed manual."
                    },
                    {
                        "engine_code": "S38B36",
                        "name": "3.6L DOHC 24V M-Power Inline-6",
                        "displacement_cc": 3535,
                        "displacement_litres": 3.6,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 232,
                        "power_rpm": "6900",
                        "torque_nm": 360,
                        "torque_rpm": "4750",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Hand-built at BMW M in Garching; individual throttle bodies."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "540i",
                        "years": {"start": 1993, "end": 1996},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed automatic"],
                        "msrp_aud_min": 142500,
                        "msrp_aud_max": 154000,
                        "fuel_consumption_l_100km": 11.8,
                        "kerb_weight_kg": 1680,
                        "standard_features": ["Leather upholstery", "Wood trim", "Electronic damper control", "Sunroof", "ABS"],
                        "notes": "V8 luxury powerhouse."
                    },
                    {
                        "badge_name": "M5 3.6",
                        "years": {"start": 1990, "end": 1994},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual"],
                        "msrp_aud_min": 168000,
                        "msrp_aud_max": 182000,
                        "fuel_consumption_l_100km": 12.5,
                        "kerb_weight_kg": 1670,
                        "standard_features": ["Turbine alloy wheels", "Nappa leather interior", "M sport steering wheel", "Self-levelling rear suspension"],
                        "notes": "The original hand-assembled four-door supercar."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M5 3.6",
                        "body_style": "4-door sedan",
                        "engine_code": "S38B36",
                        "transmission": "5-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1990,
                        "years_end": 1994,
                        "msrp_aud": 172000,
                        "power_kw": 232,
                        "torque_nm": 360,
                        "fuel_l_100km": 12.5,
                        "towing_braked_kg": 1600,
                        "notes": "Hand-crafted Motorsport legend."
                    }
                ]
            },
            {
                "series_code": "E39",
                "generation_name": "5 Series E39 & M5",
                "years": {"start": 1996, "end": 2003},
                "body_styles": ["4-door sedan", "Touring wagon"],
                "platform": "BMW E39",
                "ancap_rating": "4 stars",
                "summary": "Widely heralded as one of the finest sedans ever built. Featured all-aluminium suspension, 528i/530i inline-sixes, 540i V8, and the iconic E39 M5 with 294kW S62 4.9L V8, 6-speed manual, and limited-slip differential.",
                "engines": [
                    {
                        "engine_code": "M62B44",
                        "name": "4.4L DOHC 32V V8",
                        "displacement_cc": 4398,
                        "displacement_litres": 4.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 210,
                        "power_rpm": "5400",
                        "torque_nm": 440,
                        "torque_rpm": "3600",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "VANOS variable valve timing."
                    },
                    {
                        "engine_code": "S62B50",
                        "name": "4.9L DOHC 32V M-Power V8",
                        "displacement_cc": 4941,
                        "displacement_litres": 4.9,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 294,
                        "power_rpm": "6600",
                        "torque_nm": 500,
                        "torque_rpm": "3800",
                        "compression_ratio": "11.0:1",
                        "valvetrain": "DOHC 32-valve Double-VANOS",
                        "notes": "Individual electronically controlled throttle bodies; 7000rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "540i Executive / Sport",
                        "years": {"start": 1996, "end": 2003},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed Steptronic automatic", "6-speed manual"],
                        "msrp_aud_min": 145000,
                        "msrp_aud_max": 162900,
                        "fuel_consumption_l_100km": 12.3,
                        "kerb_weight_kg": 1660,
                        "standard_features": ["Montana leather", "Navigation display", "Glass sunroof", "Xenon headlamps"],
                        "notes": "Consummate executive grand tourer."
                    },
                    {
                        "badge_name": "M5",
                        "years": {"start": 1999, "end": 2003},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["6-speed manual (Getrag 420G)"],
                        "msrp_aud_min": 198500,
                        "msrp_aud_max": 208500,
                        "fuel_consumption_l_100km": 13.9,
                        "kerb_weight_kg": 1795,
                        "standard_features": ["18-inch Style 65 Shadow Chrome alloys", "Dual quad exhaust pipes", "Nappa Heritage leather", "Sport button with sharpened throttle", "Mechanical LSD"],
                        "notes": "0-100km/h in 5.3s. The undisputed gold standard of sports sedans."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M5",
                        "body_style": "4-door sedan",
                        "engine_code": "S62B50",
                        "transmission": "6-speed manual (Getrag 420G)",
                        "drivetrain": "RWD",
                        "years_start": 1999,
                        "years_end": 2003,
                        "msrp_aud": 204000,
                        "power_kw": 294,
                        "torque_nm": 500,
                        "fuel_l_100km": 13.9,
                        "towing_braked_kg": 1800,
                        "notes": "Naturally aspirated 400hp V8 manual sports sedan."
                    }
                ]
            },
            {
                "series_code": "E60",
                "generation_name": "5 Series E60 & M5 V10",
                "years": {"start": 2003, "end": 2010},
                "body_styles": ["4-door sedan", "Touring wagon"],
                "platform": "BMW E60",
                "ancap_rating": "5 stars",
                "summary": "Chris Bangle flame-surfacing design with aluminum front chassis structure. Highlighted by the Formula 1-inspired BMW M5 powered by the magnificent 373kW 5.0L V10 S85 engine revving to 8,250rpm.",
                "engines": [
                    {
                        "engine_code": "S85B50",
                        "name": "5.0L DOHC 40V V10 M-Power",
                        "displacement_cc": 4999,
                        "displacement_litres": 5.0,
                        "cylinders": 10,
                        "configuration": "V10",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 373,
                        "power_rpm": "7750",
                        "torque_nm": 520,
                        "torque_rpm": "6100",
                        "compression_ratio": "12.0:1",
                        "valvetrain": "DOHC 40-valve Double-VANOS",
                        "notes": "Formula 1 technology transfer; individual throttle bodies, 8250rpm redline."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "M5 V10",
                        "years": {"start": 2005, "end": 2010},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["7-speed SMG-III automated manual"],
                        "msrp_aud_min": 226900,
                        "msrp_aud_max": 242000,
                        "fuel_consumption_l_100km": 14.8,
                        "kerb_weight_kg": 1830,
                        "standard_features": ["19-inch M Radial alloys", "Variable M differential lock", "EDC electronic dampers", "Active side bolsters", "Head-up display"],
                        "notes": "0-100km/h in 4.7s. 507hp V10 scream."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M5 V10",
                        "body_style": "4-door sedan",
                        "engine_code": "S85B50",
                        "transmission": "7-speed SMG-III automated manual",
                        "drivetrain": "RWD",
                        "years_start": 2005,
                        "years_end": 2010,
                        "msrp_aud": 235000,
                        "power_kw": 373,
                        "torque_nm": 520,
                        "fuel_l_100km": 14.8,
                        "towing_braked_kg": 1800,
                        "notes": "Naturally aspirated V10 performance pinnacle."
                    }
                ]
            },
            {
                "series_code": "G30/F90",
                "generation_name": "5 Series G30 & M5 Competition",
                "years": {"start": 2017, "end": 2023},
                "body_styles": ["4-door sedan", "Touring wagon"],
                "platform": "BMW CLAR",
                "ancap_rating": "5 stars",
                "summary": "Built on the lightweight CLAR carbon core platform. Lineup featured the 530i, 540i xDrive, M550i V8, and the ferocious F90 M5 Competition packing a 460kW 4.4L twin-turbo V8 and switchable M xDrive AWD.",
                "engines": [
                    {
                        "engine_code": "S63B44T4",
                        "name": "4.4L TwinPower Turbo V8 (M5 Competition)",
                        "displacement_cc": 4395,
                        "displacement_litres": 4.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 460,
                        "power_rpm": "6000",
                        "torque_nm": 750,
                        "torque_rpm": "1800-5800",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve Valvetronic",
                        "notes": "Cross-bank exhaust manifolds and twin-scroll turbochargers."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "M5 Competition",
                        "years": {"start": 2018, "end": 2023},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed M Steptronic automatic"],
                        "msrp_aud_min": 229900,
                        "msrp_aud_max": 273900,
                        "fuel_consumption_l_100km": 10.6,
                        "kerb_weight_kg": 1895,
                        "standard_features": ["20-inch forged M alloys", "M Carbon ceramic brakes option", "Carbon fibre roof", "Bowers & Wilkins Diamond surround sound", "M xDrive with 2WD rear-drive drift mode"],
                        "notes": "0-100km/h in 3.3s. Supercar obliterator."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M5 Competition",
                        "body_style": "4-door sedan",
                        "engine_code": "S63B44T4",
                        "transmission": "8-speed M Steptronic automatic",
                        "drivetrain": "AWD",
                        "years_start": 2018,
                        "years_end": 2023,
                        "msrp_aud": 259900,
                        "power_kw": 460,
                        "torque_nm": 750,
                        "fuel_l_100km": 10.6,
                        "towing_braked_kg": 2000,
                        "notes": "460kW all-wheel drive M flagship."
                    }
                ]
            }
        ]
    },

    "bmw/x5": {
        "make_slug": "bmw",
        "model_slug": "x5",
        "name": "X5",
        "vehicle_type": "Large Luxury SUV",
        "segment": "Large Luxury SUV",
        "years_sold_au": {"start": 2000, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The vehicle that redefined the luxury SUV category in Australia. Originating in 2000 as the world's first true Sports Activity Vehicle (SAV) with monocoque construction and car-like handling, the BMW X5 has dominated Australian luxury SUV sales across four generations.",
        "australian_market_notes": "Launched in Australia in late 2000 (E53). The six-cylinder diesel models (3.0d / xDrive30d) established an unprecedented reputation as long-distance Australian touring wagons, capable of effortless country overtaking and heavy horse-float and caravan towing. The X5 M transformed the super-SUV segment.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "E53",
                "generation_name": "X5 First Generation (E53)",
                "years": {"start": 2000, "end": 2006},
                "body_styles": ["5-door SUV"],
                "platform": "BMW E53",
                "ancap_rating": "5 stars",
                "summary": "Pioneered car-like monocoque SUV chassis dynamics. Offered with 3.0i petrol, 3.0d turbo-diesel, 4.4i V8, and the high-output 4.6is / 4.8is performance flagships with 265kW.",
                "engines": [
                    {
                        "engine_code": "M57D30",
                        "name": "3.0L Turbo Diesel Inline-6",
                        "displacement_cc": 2926,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 160,
                        "power_rpm": "4000",
                        "torque_nm": 500,
                        "torque_rpm": "2000-2750",
                        "compression_ratio": "17.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Common-rail diesel powerhouse that captured the Australian market."
                    },
                    {
                        "engine_code": "N62B48",
                        "name": "4.8L DOHC 32V V8 (4.8is)",
                        "displacement_cc": 4799,
                        "displacement_litres": 4.8,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 265,
                        "power_rpm": "6200",
                        "torque_nm": 500,
                        "torque_rpm": "3500",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 32-valve Valvetronic",
                        "notes": "Performance hero with air suspension and 20-inch wheels."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "3.0d",
                        "years": {"start": 2001, "end": 2006},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["5-speed automatic", "6-speed automatic"],
                        "msrp_aud_min": 79900,
                        "msrp_aud_max": 93500,
                        "fuel_consumption_l_100km": 8.6,
                        "kerb_weight_kg": 2095,
                        "standard_features": ["Leather trim", "Dynamic Stability Control", "Hill Descent Control", "Split tailgate"],
                        "notes": "Australia's favorite luxury tow vehicle."
                    },
                    {
                        "badge_name": "4.8is",
                        "years": {"start": 2004, "end": 2006},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed automatic"],
                        "msrp_aud_min": 158500,
                        "msrp_aud_max": 163000,
                        "fuel_consumption_l_100km": 13.5,
                        "kerb_weight_kg": 2200,
                        "standard_features": ["20-inch V-spoke alloys", "Two-axle air suspension", "Sport body styling", "Panoramic glass sunroof"],
                        "notes": "Precursor to the modern X5 M."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "3.0d",
                        "body_style": "5-door SUV",
                        "engine_code": "M57D30",
                        "transmission": "6-speed automatic",
                        "drivetrain": "AWD",
                        "years_start": 2004,
                        "years_end": 2006,
                        "msrp_aud": 86900,
                        "power_kw": 160,
                        "torque_nm": 500,
                        "fuel_l_100km": 8.6,
                        "towing_braked_kg": 2700,
                        "notes": "Facelifted E53 with xDrive and 6-speed ZF auto."
                    }
                ]
            },
            {
                "series_code": "E70",
                "generation_name": "X5 Second Generation (E70)",
                "years": {"start": 2007, "end": 2013},
                "body_styles": ["5-door SUV", "7-seat SUV"],
                "platform": "BMW E70",
                "ancap_rating": "5 stars",
                "summary": "Introduced available third-row 7-seat packaging, Adaptive Drive active anti-roll bars, iDrive, and the inaugural BMW X5 M powered by a 408kW 4.4L twin-turbo V8.",
                "engines": [
                    {
                        "engine_code": "N57D30",
                        "name": "3.0L Turbo Diesel Inline-6 (xDrive30d)",
                        "displacement_cc": 2993,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 180,
                        "power_rpm": "4000",
                        "torque_nm": 540,
                        "torque_rpm": "1750-3000",
                        "compression_ratio": "16.5:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "All-aluminium block, piezo common-rail injection."
                    },
                    {
                        "engine_code": "S63B44A",
                        "name": "4.4L TwinPower V8 (X5 M)",
                        "displacement_cc": 4395,
                        "displacement_litres": 4.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 408,
                        "power_rpm": "6000",
                        "torque_nm": 680,
                        "torque_rpm": "1500-5650",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "First all-wheel-drive M car in history."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "xDrive30d",
                        "years": {"start": 2007, "end": 2013},
                        "body_styles": ["5-door SUV", "7-seat SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed automatic", "8-speed automatic"],
                        "msrp_aud_min": 86900,
                        "msrp_aud_max": 96900,
                        "fuel_consumption_l_100km": 7.4,
                        "kerb_weight_kg": 2150,
                        "standard_features": ["18-inch alloys", "Nevada leather", "Park Distance Control", "Dual-zone climate"],
                        "notes": "Australia's top-selling luxury SUV."
                    },
                    {
                        "badge_name": "X5 M",
                        "years": {"start": 2009, "end": 2013},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed M Sports automatic"],
                        "msrp_aud_min": 172900,
                        "msrp_aud_max": 185000,
                        "fuel_consumption_l_100km": 13.9,
                        "kerb_weight_kg": 2380,
                        "standard_features": ["20-inch M light alloys", "M Dynamic Mode", "Adaptive Drive", "Quad exhaust tips"],
                        "notes": "0-100km/h in 4.7s. 555hp super SUV."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "xDrive30d",
                        "body_style": "5-door SUV",
                        "engine_code": "N57D30",
                        "transmission": "8-speed automatic",
                        "drivetrain": "AWD",
                        "years_start": 2010,
                        "years_end": 2013,
                        "msrp_aud": 92900,
                        "power_kw": 180,
                        "torque_nm": 540,
                        "fuel_l_100km": 7.4,
                        "towing_braked_kg": 2700,
                        "notes": "Facelifted LCI model with 8-speed ZF auto."
                    }
                ]
            },
            {
                "series_code": "G05",
                "generation_name": "X5 Fourth Generation (G05)",
                "years": {"start": 2018, "end": "Present"},
                "body_styles": ["5-door SUV"],
                "platform": "BMW CLAR",
                "ancap_rating": "5 stars",
                "summary": "Built on CLAR platform with optional two-axle air suspension, off-road package, xDrive30d, plug-in hybrid xDrive45e/50e, M50i/M60i V8, and the mighty 460kW X5 M Competition.",
                "engines": [
                    {
                        "engine_code": "B57D30",
                        "name": "3.0L Turbo Diesel Inline-6 (xDrive30d)",
                        "displacement_cc": 2993,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 195,
                        "power_rpm": "4000",
                        "torque_nm": 620,
                        "torque_rpm": "2000-2500",
                        "compression_ratio": "16.5:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Later upgraded to 210kW with 48V mild-hybrid system."
                    },
                    {
                        "engine_code": "S63B44B",
                        "name": "4.4L TwinPower V8 (X5 M Competition)",
                        "displacement_cc": 4395,
                        "displacement_litres": 4.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 460,
                        "power_rpm": "6000",
                        "torque_nm": 750,
                        "torque_rpm": "1800-5800",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "625hp Competition specification with active M differential."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "xDrive30d M Sport",
                        "years": {"start": 2018, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 112900,
                        "msrp_aud_max": 141900,
                        "fuel_consumption_l_100km": 7.2,
                        "kerb_weight_kg": 2185,
                        "standard_features": ["20-inch M alloys", "Live Cockpit Professional", "Vernasca leather", "Panoramic glass roof", "Driving Assistant Professional"],
                        "notes": "Dominant luxury SUV choice in corporate and regional Australia."
                    },
                    {
                        "badge_name": "X5 M Competition",
                        "years": {"start": 2020, "end": "Present"},
                        "body_styles": ["5-door SUV"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed M Steptronic automatic"],
                        "msrp_aud_min": 212900,
                        "msrp_aud_max": 247900,
                        "fuel_consumption_l_100km": 12.5,
                        "kerb_weight_kg": 2310,
                        "standard_features": ["21/22-inch staggered M alloys", "M Sport exhaust", "Carbon fibre trim", "Laserlight headlights", "Bowers & Wilkins Diamond sound"],
                        "notes": "0-100km/h in 3.8s. Unrivalled luxury performance."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "xDrive30d M Sport",
                        "body_style": "5-door SUV",
                        "engine_code": "B57D30",
                        "transmission": "8-speed automatic",
                        "drivetrain": "AWD",
                        "years_start": 2018,
                        "years_end": "Present",
                        "msrp_aud": 124900,
                        "power_kw": 195,
                        "torque_nm": 620,
                        "fuel_l_100km": 7.2,
                        "towing_braked_kg": 3500,
                        "notes": "Benchmark 3500kg braked towing luxury SUV."
                    },
                    {
                        "badge_name": "X5 M Competition",
                        "body_style": "5-door SUV",
                        "engine_code": "S63B44B",
                        "transmission": "8-speed M Steptronic automatic",
                        "drivetrain": "AWD",
                        "years_start": 2020,
                        "years_end": "Present",
                        "msrp_aud": 229900,
                        "power_kw": 460,
                        "torque_nm": 750,
                        "fuel_l_100km": 12.5,
                        "towing_braked_kg": 3000,
                        "notes": "460kW super-SUV flagship."
                    }
                ]
            }
        ]
    },

    "mercedes-benz/e-class": {
        "make_slug": "mercedes-benz",
        "model_slug": "e-class",
        "name": "E-Class",
        "vehicle_type": "Sedan / Wagon / Coupe / Cabriolet",
        "segment": "Large Luxury Car",
        "years_sold_au": {"start": 1968, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The heartbeat of Mercedes-Benz in Australia. From the virtually indestructible W114/W115 and W123 that conquered outback roads and taxi fleets, through the peerless Bruno Sacco W124, to supercharged V8 E55 AMG and twin-turbo 450kW E63 S AMG monsters.",
        "australian_market_notes": "First sold as the 'Stroke 8' (W114/W115) in 1968. The W123 earned iconic status in Australia for racking up millions of kilometers with zero rattles, while the W124 300E and Porsche-assembled 500E set luxury performance benchmarks. Australia remains one of AMG's highest market-share territories globally.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "W123",
                "generation_name": "E-Class W123 Series",
                "years": {"start": 1976, "end": 1985},
                "body_styles": ["4-door sedan", "Coupe", "Estate wagon"],
                "platform": "Mercedes-Benz W123",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Legendary engineered-like-no-other-car-in-the-world durability. Highlights included 230E petrol, 280E twin-cam inline-six, and the bombproof OM617 5-cylinder 300D diesel.",
                "engines": [
                    {
                        "engine_code": "M110",
                        "name": "2.8L DOHC Inline-6",
                        "displacement_cc": 2746,
                        "displacement_litres": 2.8,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 136,
                        "power_rpm": "5800",
                        "torque_nm": 240,
                        "torque_rpm": "4500",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 12-valve",
                        "notes": "Bosch K-Jetronic mechanical fuel injection; iconic twin-cam howl."
                    },
                    {
                        "engine_code": "OM617",
                        "name": "3.0L SOHC Diesel Inline-5",
                        "displacement_cc": 3005,
                        "displacement_litres": 3.0,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Diesel",
                        "power_kw": 59,
                        "power_rpm": "4000",
                        "torque_nm": 172,
                        "torque_rpm": "2400",
                        "compression_ratio": "21.0:1",
                        "valvetrain": "SOHC 10-valve",
                        "notes": "Legendary million-kilometer durability; mechanical inline Bosch injection pump."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "280E",
                        "years": {"start": 1976, "end": 1985},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed automatic", "4-speed manual"],
                        "msrp_aud_min": 24900,
                        "msrp_aud_max": 41200,
                        "fuel_consumption_l_100km": 12.2,
                        "kerb_weight_kg": 1475,
                        "standard_features": ["MB-Tex or velour upholstery", "Zebrano wood console", "Power steering", "Four-wheel disc brakes"],
                        "notes": "Australia's premier executive transport of the late 1970s and 1980s."
                    },
                    {
                        "badge_name": "300D",
                        "years": {"start": 1976, "end": 1985},
                        "body_styles": ["4-door sedan", "Estate wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed automatic"],
                        "msrp_aud_min": 26500,
                        "msrp_aud_max": 42900,
                        "fuel_consumption_l_100km": 9.5,
                        "kerb_weight_kg": 1505,
                        "standard_features": ["Glow plug system", "Central locking", "Dual exterior mirrors", "Rigid passenger cell"],
                        "notes": "Celebrated worldwide and in Australia for indestructible engineering."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "280E",
                        "body_style": "4-door sedan",
                        "engine_code": "M110",
                        "transmission": "4-speed automatic",
                        "drivetrain": "RWD",
                        "years_start": 1976,
                        "years_end": 1985,
                        "msrp_aud": 33900,
                        "power_kw": 136,
                        "torque_nm": 240,
                        "fuel_l_100km": 12.2,
                        "towing_braked_kg": 1500,
                        "notes": "Top-specification Australian delivered W123 petrol sedan."
                    }
                ]
            },
            {
                "series_code": "W124",
                "generation_name": "E-Class W124 Series",
                "years": {"start": 1985, "end": 1995},
                "body_styles": ["4-door sedan", "Coupe", "Cabriolet", "Estate wagon"],
                "platform": "Mercedes-Benz W124",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Masterpiece designed by Bruno Sacco featuring innovative 5-link independent rear suspension, aerodynamic drag Cd of 0.29, 300E/320E inline-sixes, and the legendary hand-built 500E (engineered and assembled in partnership with Porsche).",
                "engines": [
                    {
                        "engine_code": "M103",
                        "name": "3.0L SOHC Inline-6",
                        "displacement_cc": 2960,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 132,
                        "power_rpm": "5700",
                        "torque_nm": 255,
                        "torque_rpm": "4400",
                        "compression_ratio": "9.2:1",
                        "valvetrain": "SOHC 12-valve",
                        "notes": "Smooth KE-Jetronic injected six, standard on Australian 300E."
                    },
                    {
                        "engine_code": "M119",
                        "name": "5.0L DOHC 32V V8 (500E)",
                        "displacement_cc": 4973,
                        "displacement_litres": 5.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 240,
                        "power_rpm": "5700",
                        "torque_nm": 480,
                        "torque_rpm": "3900",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Porsche-engineered and hand-assembled at Rossle-Bau in Zuffenhausen; flared wheel arches."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "300E / E300",
                        "years": {"start": 1986, "end": 1995},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed automatic"],
                        "msrp_aud_min": 89500,
                        "msrp_aud_max": 129000,
                        "fuel_consumption_l_100km": 10.8,
                        "kerb_weight_kg": 1400,
                        "standard_features": ["ABS brakes", "Zebrano wood trim", "Electric sunroof", "Automatic climate control", "Driver airbag"],
                        "notes": "The defining executive car of corporate Australia during the late 80s."
                    },
                    {
                        "badge_name": "500E / E500",
                        "years": {"start": 1991, "end": 1994},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed automatic"],
                        "msrp_aud_min": 198000,
                        "msrp_aud_max": 235000,
                        "fuel_consumption_l_100km": 13.5,
                        "kerb_weight_kg": 1710,
                        "standard_features": ["Recaro 4-seater sport interior", "Flared front and rear wheel arches", "SL500 suspension and brakes", "ASR traction control"],
                        "notes": "The 'Iron Fist in a Velvet Glove'. Highly prized Australian collector's icon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "500E / E500",
                        "body_style": "4-door sedan",
                        "engine_code": "M119",
                        "transmission": "4-speed automatic",
                        "drivetrain": "RWD",
                        "years_start": 1991,
                        "years_end": 1994,
                        "msrp_aud": 215000,
                        "power_kw": 240,
                        "torque_nm": 480,
                        "fuel_l_100km": 13.5,
                        "towing_braked_kg": 1500,
                        "notes": "Porsche-built 5.0L V8 super-sedan."
                    }
                ]
            },
            {
                "series_code": "W211",
                "generation_name": "E-Class W211 Series",
                "years": {"start": 2002, "end": 2009},
                "body_styles": ["4-door sedan", "Estate wagon"],
                "platform": "Mercedes-Benz W211",
                "ancap_rating": "5 stars",
                "summary": "Elegant aerodynamic redesign featuring Airmatic DC suspension. Highlighted by the fearsome E55 AMG (350kW supercharged 5.4L V8) and later the naturally aspirated 6.2L V8 E63 AMG.",
                "engines": [
                    {
                        "engine_code": "M113ML",
                        "name": "5.4L Supercharged SOHC V8 (E55 AMG)",
                        "displacement_cc": 5439,
                        "displacement_litres": 5.4,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Supercharged",
                        "fuel_type": "Petrol",
                        "power_kw": 350,
                        "power_rpm": "6100",
                        "torque_nm": 700,
                        "torque_rpm": "2650-4500",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "SOHC 24-valve (3 valves per cylinder)",
                        "notes": "Lysholm twin-screw supercharger; devastating rolling acceleration."
                    },
                    {
                        "engine_code": "M156",
                        "name": "6.2L DOHC 32V V8 (E63 AMG)",
                        "displacement_cc": 6208,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 378,
                        "power_rpm": "6800",
                        "torque_nm": 630,
                        "torque_rpm": "5200",
                        "compression_ratio": "11.3:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "First engine designed from the ground up by AMG in Affalterbach."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "E55 AMG",
                        "years": {"start": 2003, "end": 2006},
                        "body_styles": ["4-door sedan", "Estate wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed AMG Speedshift automatic"],
                        "msrp_aud_min": 219900,
                        "msrp_aud_max": 232000,
                        "fuel_consumption_l_100km": 12.9,
                        "kerb_weight_kg": 1835,
                        "standard_features": ["18-inch AMG 5-spoke alloys", "AMG Airmatic sport suspension", "8-piston front brake calipers", "Nappa nubuck leather"],
                        "notes": "0-100km/h in 4.5s. Muscle car annihilator."
                    },
                    {
                        "badge_name": "E63 AMG",
                        "years": {"start": 2006, "end": 2009},
                        "body_styles": ["4-door sedan", "Estate wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["7-speed 7G-Tronic AMG Speedshift"],
                        "msrp_aud_min": 227600,
                        "msrp_aud_max": 239900,
                        "fuel_consumption_l_100km": 14.3,
                        "kerb_weight_kg": 1840,
                        "standard_features": ["18-inch AMG multi-spoke wheels", "Race start function", "Harman Kardon Logic 7 sound", "AMG quad exhaust"],
                        "notes": "High-revving 6.2L naturally aspirated masterpiece."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "E55 AMG",
                        "body_style": "4-door sedan",
                        "engine_code": "M113ML",
                        "transmission": "5-speed AMG Speedshift automatic",
                        "drivetrain": "RWD",
                        "years_start": 2003,
                        "years_end": 2006,
                        "msrp_aud": 224000,
                        "power_kw": 350,
                        "torque_nm": 700,
                        "fuel_l_100km": 12.9,
                        "towing_braked_kg": 1900,
                        "notes": "350kW supercharged V8 torque titan."
                    }
                ]
            },
            {
                "series_code": "W213",
                "generation_name": "E-Class W213 Series & E63 S AMG",
                "years": {"start": 2016, "end": 2023},
                "body_styles": ["4-door sedan", "Coupe", "Cabriolet", "Estate wagon"],
                "platform": "Mercedes-Benz MRA",
                "ancap_rating": "5 stars",
                "summary": "Built on the MRA lightweight modular platform. Featured dual 12.3-inch widescreen cockpit displays, Drive Pilot semi-autonomous driving, and the almighty AMG E63 S 4MATIC+ with 450kW, 850Nm, and pure rear-wheel-drive Drift Mode.",
                "engines": [
                    {
                        "engine_code": "M177",
                        "name": "4.0L BiTurbo V8 (E63 S AMG)",
                        "displacement_cc": 3982,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 450,
                        "power_rpm": "5750-6500",
                        "torque_nm": 850,
                        "torque_rpm": "2500-4500",
                        "compression_ratio": "8.6:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "'Hot inside V' twin-scroll turbochargers and cylinder deactivation."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "E300 / E350",
                        "years": {"start": 2016, "end": 2023},
                        "body_styles": ["4-door sedan", "Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["9-speed 9G-Tronic automatic"],
                        "msrp_aud_min": 107900,
                        "msrp_aud_max": 133900,
                        "fuel_consumption_l_100km": 7.3,
                        "kerb_weight_kg": 1655,
                        "standard_features": ["Dual widescreen cockpit", "Multibeam LED headlights", "Burmester sound system", "Driving Assistance Package Plus"],
                        "notes": "Core executive fleet choice."
                    },
                    {
                        "badge_name": "AMG E63 S 4MATIC+",
                        "years": {"start": 2017, "end": 2023},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "AWD",
                        "transmissions": ["9-speed AMG Speedshift MCT"],
                        "msrp_aud_min": 239611,
                        "msrp_aud_max": 272400,
                        "fuel_consumption_l_100km": 10.8,
                        "kerb_weight_kg": 1955,
                        "standard_features": ["20-inch AMG cross-spoke forged wheels", "4MATIC+ variable AWD with Drift Mode", "AMG Performance sports exhaust", "Nappa exclusive leather"],
                        "notes": "0-100km/h in 3.4 seconds. King of the executive autobahn missiles."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "AMG E63 S 4MATIC+",
                        "body_style": "4-door sedan",
                        "engine_code": "M177",
                        "transmission": "9-speed AMG Speedshift MCT",
                        "drivetrain": "AWD",
                        "years_start": 2017,
                        "years_end": 2023,
                        "msrp_aud": 252900,
                        "power_kw": 450,
                        "torque_nm": 850,
                        "fuel_l_100km": 10.8,
                        "towing_braked_kg": 2100,
                        "notes": "450kW all-wheel drive flagship with rear-drive Drift Mode."
                    }
                ]
            }
        ]
    },

    "mercedes-benz/g-class": {
        "make_slug": "mercedes-benz",
        "model_slug": "g-class",
        "name": "G-Class (Geländewagen)",
        "vehicle_type": "Off-Road 4x4 / Luxury SUV / Military Transport",
        "segment": "Heavy Duty 4WD / Upper Large Luxury SUV",
        "years_sold_au": {"start": 1982, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The immortal Mercedes-Benz Geländewagen. Originating as a relentless military off-roader with three locking differentials, the G-Class became a trusted explorer in the Australian outback and was selected by the Australian Defence Force under Project Overlander Land 121, resulting in over 2,000 bespoke Australian Army 4x4 and 6x6 vehicles. Concurrently, the civilian W463 morphed into the ultimate status symbol through the roaring twin-turbo V8 AMG G63.",
        "australian_market_notes": "First sold in Australia in 1982 (W460 280GE and 300GD). In 2008, the Australian Defence Force awarded Mercedes-Benz the Land 121 contract, purchasing over 2,000 W461 G-Wagens in 4x4 and Australian-exclusive 6x6 configurations. The G63 AMG accounts for the vast majority of civilian Australian sales.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "W460",
                "generation_name": "G-Class W460 Series",
                "years": {"start": 1982, "end": 1991},
                "body_styles": ["2-door SWB wagon", "4-door LWB wagon", "Cab-chassis"],
                "platform": "Mercedes-Benz W460",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The pure original Geländewagen. Ladder chassis, live axles front and rear, part-time 4WD, mechanical differential locks, and bulletproof M110 petrol and OM617 diesel engines.",
                "engines": [
                    {
                        "engine_code": "M110",
                        "name": "2.8L DOHC Inline-6 (280GE)",
                        "displacement_cc": 2746,
                        "displacement_litres": 2.8,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 115,
                        "power_rpm": "5250",
                        "torque_nm": 226,
                        "torque_rpm": "4250",
                        "compression_ratio": "8.0:1",
                        "valvetrain": "DOHC 12-valve",
                        "notes": "Low-compression engine suited to Australian outback fuels."
                    },
                    {
                        "engine_code": "OM617",
                        "name": "3.0L SOHC Diesel Inline-5 (300GD)",
                        "displacement_cc": 2998,
                        "displacement_litres": 3.0,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Diesel",
                        "power_kw": 65,
                        "power_rpm": "4400",
                        "torque_nm": 172,
                        "torque_rpm": "2400",
                        "compression_ratio": "21.0:1",
                        "valvetrain": "SOHC 10-valve",
                        "notes": "Indestructible tractor-like diesel for rural and mining exploration."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "280GE",
                        "years": {"start": 1982, "end": 1991},
                        "body_styles": ["2-door SWB wagon", "4-door LWB wagon"],
                        "drivetrain": "4WD",
                        "transmissions": ["4-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 31950,
                        "msrp_aud_max": 47900,
                        "fuel_consumption_l_100km": 15.5,
                        "kerb_weight_kg": 1980,
                        "standard_features": ["Dual mechanical diff locks", "Dual fuel tanks option", "Steel wheels", "Rubber floor mats"],
                        "notes": "The foundation G-Wagen in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "280GE",
                        "body_style": "4-door LWB wagon",
                        "engine_code": "M110",
                        "transmission": "4-speed manual",
                        "drivetrain": "4WD",
                        "years_start": 1982,
                        "years_end": 1991,
                        "msrp_aud": 38900,
                        "power_kw": 115,
                        "torque_nm": 226,
                        "fuel_l_100km": 15.5,
                        "towing_braked_kg": 2500,
                        "notes": "Australian outback explorer specification."
                    }
                ]
            },
            {
                "series_code": "W461",
                "generation_name": "G-Class W461 & ADF Land 121 (4x4 & 6x6)",
                "years": {"start": 2009, "end": "Present"},
                "body_styles": ["4-door wagon", "Single-cab chassis", "Dual-cab chassis", "6x6 Military Cab-Chassis"],
                "platform": "Mercedes-Benz W461 Heavy Duty",
                "ancap_rating": "Unrated (Military/Commercial)",
                "summary": "Heavy-duty commercial and military chassis chosen by the Australian Defence Force under Project Overlander Land 121. Over 2,000 units delivered to the Australian Army in 4x4 and bespoke 6x6 cab-chassis and ambulance configurations, powered by the OM642 3.0L turbo-diesel V6 (135kW 400Nm) with portal axles on 6x6 and dual snorkels. Civilian G300 CDI Professional sold from 2016-2019.",
                "engines": [
                    {
                        "engine_code": "OM642",
                        "name": "3.0L V6 Turbo Diesel",
                        "displacement_cc": 2987,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 135,
                        "power_rpm": "3800",
                        "torque_nm": 400,
                        "torque_rpm": "1600-2600",
                        "compression_ratio": "17.7:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Heavy-duty de-rated tune for high-sulfur and military fuel endurance."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Australian Army G-Wagen 4x4 & 6x6",
                        "years": {"start": 2009, "end": "Present"},
                        "body_styles": ["Single-cab chassis", "Dual-cab chassis", "6x6 Military Cab-Chassis"],
                        "drivetrain": "4WD / 6WD",
                        "transmissions": ["5-speed automatic with transfer case"],
                        "msrp_aud_min": 140000,
                        "msrp_aud_max": 250000,
                        "fuel_consumption_l_100km": 14.5,
                        "kerb_weight_kg": 3200,
                        "standard_features": ["Triple locking diffs (4x4) / Five locking diffs (6x6)", "Portal axles (6x6)", "7000kg GVM (6x6)", "Run-flat tyres", "Heavy-duty steel bullbar and winch"],
                        "notes": "Project Overlander Land 121 backbone of the Australian Defence Force."
                    },
                    {
                        "badge_name": "G300 CDI Professional",
                        "years": {"start": 2016, "end": 2019},
                        "body_styles": ["Single-cab chassis", "4-door wagon"],
                        "drivetrain": "4WD",
                        "transmissions": ["5-speed automatic"],
                        "msrp_aud_min": 109900,
                        "msrp_aud_max": 119900,
                        "fuel_consumption_l_100km": 11.9,
                        "kerb_weight_kg": 2560,
                        "standard_features": ["16-inch heavy-duty steel wheels", "Factory snorkel", "Front bullbar", "Three 100% diff locks", "Water-drainable rubber floors"],
                        "notes": "Civilian-delivered heavy-duty workhorse."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "G300 CDI Professional",
                        "body_style": "Single-cab chassis",
                        "engine_code": "OM642",
                        "transmission": "5-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2016,
                        "years_end": 2019,
                        "msrp_aud": 119900,
                        "power_kw": 135,
                        "torque_nm": 400,
                        "fuel_l_100km": 11.9,
                        "towing_braked_kg": 3200,
                        "notes": "Heavy-duty Australian market cab-chassis."
                    }
                ]
            },
            {
                "series_code": "W463",
                "generation_name": "G-Class W463 (Civilian Luxury & AMG)",
                "years": {"start": 1990, "end": 2018},
                "body_styles": ["4-door wagon", "Cabriolet"],
                "platform": "Mercedes-Benz W463",
                "ancap_rating": "Unrated",
                "summary": "Transformed the G-Wagen from military workhorse into ultra-luxury automotive royalty. Featured permanent all-wheel drive with triple electro-pneumatic differential locks, G500 V8, G350 BlueTEC diesel, and the iconic supercharged G55 and twin-turbo G63 AMG.",
                "engines": [
                    {
                        "engine_code": "M157",
                        "name": "5.5L BiTurbo V8 (G63 AMG)",
                        "displacement_cc": 5461,
                        "displacement_litres": 5.5,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 420,
                        "power_rpm": "5500",
                        "torque_nm": 760,
                        "torque_rpm": "2000-5000",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Side-exit dual exhaust pipes beneath rear doors; thunderous exhaust note."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "G63 AMG",
                        "years": {"start": 2012, "end": 2018},
                        "body_styles": ["4-door wagon"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed AMG Speedshift Plus"],
                        "msrp_aud_min": 229900,
                        "msrp_aud_max": 252900,
                        "fuel_consumption_l_100km": 13.8,
                        "kerb_weight_kg": 2550,
                        "standard_features": ["20-inch AMG 5-twin-spoke alloys", "Side-exit twin chrome exhausts", "designo leather upholstery", "Triple locking differential switches"],
                        "notes": "0-100km/h in 5.4s. The definitive luxury status symbol in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "G63 AMG",
                        "body_style": "4-door wagon",
                        "engine_code": "M157",
                        "transmission": "7-speed AMG Speedshift Plus",
                        "drivetrain": "AWD",
                        "years_start": 2012,
                        "years_end": 2018,
                        "msrp_aud": 239900,
                        "power_kw": 420,
                        "torque_nm": 760,
                        "fuel_l_100km": 13.8,
                        "towing_braked_kg": 3500,
                        "notes": "5.5L twin-turbo V8 side-pipe icon."
                    }
                ]
            },
            {
                "series_code": "W463 Gen 2",
                "generation_name": "G-Class Second Generation & AMG G63",
                "years": {"start": 2018, "end": "Present"},
                "body_styles": ["4-door wagon"],
                "platform": "Mercedes-Benz W463 Gen 2",
                "ancap_rating": "5 stars",
                "summary": "Completely redesigned from the ground up: 121mm wider body, independent double-wishbone front suspension, electromechanical rack-and-pinion steering, Widescreen Cockpit, and the 430kW 4.0L BiTurbo AMG G63.",
                "engines": [
                    {
                        "engine_code": "M177",
                        "name": "4.0L BiTurbo V8 (AMG G63)",
                        "displacement_cc": 3982,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 430,
                        "power_rpm": "6000",
                        "torque_nm": 850,
                        "torque_rpm": "2500-3500",
                        "compression_ratio": "8.6:1",
                        "valvetrain": "DOHC 32-valve",
                        "notes": "Twin hot-V turbochargers with side-pipe sports exhausts."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "AMG G63",
                        "years": {"start": 2018, "end": "Present"},
                        "body_styles": ["4-door wagon"],
                        "drivetrain": "AWD",
                        "transmissions": ["9-speed AMG Speedshift TCT"],
                        "msrp_aud_min": 247700,
                        "msrp_aud_max": 365900,
                        "fuel_consumption_l_100km": 13.1,
                        "kerb_weight_kg": 2560,
                        "standard_features": ["22-inch forged AMG cross-spoke wheels", "Side-exit sports exhaust", "Widescreen cockpit", "AMG Ride Control adaptive dampers", "Burmester surround sound"],
                        "notes": "0-100km/h in 4.5 seconds. Australia's most sought-after luxury performance off-roader."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "AMG G63",
                        "body_style": "4-door wagon",
                        "engine_code": "M177",
                        "transmission": "9-speed AMG Speedshift TCT",
                        "drivetrain": "AWD",
                        "years_start": 2018,
                        "years_end": "Present",
                        "msrp_aud": 315000,
                        "power_kw": 430,
                        "torque_nm": 850,
                        "fuel_l_100km": 13.1,
                        "towing_braked_kg": 3500,
                        "notes": "Independent front suspension 430kW super-SUV."
                    }
                ]
            }
        ]
    },

    "audi/a3-s3-rs3": {
        "make_slug": "audi",
        "model_slug": "a3-s3-rs3",
        "name": "A3, S3 & RS3",
        "vehicle_type": "Hatchback (Sportback) / Sedan / Cabriolet",
        "segment": "Small Luxury Sports Car",
        "years_sold_au": {"start": 1996, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The pioneer of the premium compact segment in Australia. Spanning four generations (8L, 8P, 8V, and 8Y), the A3 introduced luxury hatchback packaging and quattro all-wheel drive, reaching high-performance zeniths with the S3 quattro and the spine-tingling 2.5-litre turbocharged inline-5 Audi RS3 producing 294kW.",
        "australian_market_notes": "First sold in Australia in 1996 (8L). The first-generation S3 arrived in 2000, quickly winning enthusiast admiration. The RS3 arrived in 2012 (8P Sportback) with Audi's iconic turbocharged five-cylinder engine, whose heritage traces directly to the legendary Group B Audi quattro rally cars. Australia remains one of the largest global markets for S3 and RS3 models per capita.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "8L",
                "generation_name": "A3 & S3 First Generation (Typ 8L)",
                "years": {"start": 1996, "end": 2003},
                "body_styles": ["3-door hatchback", "5-door hatchback"],
                "platform": "Volkswagen Group PQ34",
                "ancap_rating": "4 stars",
                "summary": "Introduced premium German finish to the compact class. Highlighted by the original S3 quattro powered by a 1.8-litre 20-valve turbo with Haldex AWD and flared front and rear arches.",
                "engines": [
                    {
                        "engine_code": "APY/BAM",
                        "name": "1.8L 20V Turbo Petrol (S3)",
                        "displacement_cc": 1781,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 154,
                        "power_rpm": "5800",
                        "torque_nm": 270,
                        "torque_rpm": "2100-5000",
                        "compression_ratio": "9.0:1",
                        "valvetrain": "DOHC 20-valve (5 valves per cylinder)",
                        "notes": "Twin intercoolers, K04 turbocharger; upgraded to 165kW BAM in late models."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "S3 quattro",
                        "years": {"start": 2000, "end": 2003},
                        "body_styles": ["3-door hatchback"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual"],
                        "msrp_aud_min": 65900,
                        "msrp_aud_max": 69900,
                        "fuel_consumption_l_100km": 8.9,
                        "kerb_weight_kg": 1375,
                        "standard_features": ["17-inch Avus alloys", "Recaro electric leather sports seats", "Bose sound system", "quattro all-wheel drive"],
                        "notes": "The original compact executive pocket rocket."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "S3 quattro",
                        "body_style": "3-door hatchback",
                        "engine_code": "APY/BAM",
                        "transmission": "6-speed manual",
                        "drivetrain": "AWD",
                        "years_start": 2000,
                        "years_end": 2003,
                        "msrp_aud": 67900,
                        "power_kw": 154,
                        "torque_nm": 270,
                        "fuel_l_100km": 8.9,
                        "towing_braked_kg": 1400,
                        "notes": "1.8T 20V manual quattro hot hatch."
                    }
                ]
            },
            {
                "series_code": "8P",
                "generation_name": "A3, S3 & RS3 Second Generation (Typ 8P)",
                "years": {"start": 2003, "end": 2012},
                "body_styles": ["3-door hatchback", "5-door Sportback", "Cabriolet"],
                "platform": "Volkswagen Group PQ35",
                "ancap_rating": "4 stars",
                "summary": "Pioneered the Sportback body style and dual-clutch S tronic transmission. Featured 2.0 TFSI, 3.2 VR6, S3 quattro (188kW), and the debut of the RS3 Sportback with the 250kW 2.5L 5-cylinder turbo.",
                "engines": [
                    {
                        "engine_code": "BHZ/CDLC",
                        "name": "2.0L TFSI Turbo Petrol (S3)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 188,
                        "power_rpm": "6000",
                        "torque_nm": 330,
                        "torque_rpm": "2400-5200",
                        "compression_ratio": "9.8:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA113 iron-block engine with reinforced conrods and K04 turbo."
                    },
                    {
                        "engine_code": "CEPA",
                        "name": "2.5L TFSI Inline-5 Turbo (RS3)",
                        "displacement_cc": 2480,
                        "displacement_litres": 2.5,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 250,
                        "power_rpm": "5400-6500",
                        "torque_nm": 450,
                        "torque_rpm": "1600-5300",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 20-valve",
                        "notes": "Compacted graphite iron (CGI) block; 1-2-4-5-3 firing order soundtrack."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "S3 quattro",
                        "years": {"start": 2007, "end": 2012},
                        "body_styles": ["3-door hatchback", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual", "6-speed S tronic"],
                        "msrp_aud_min": 65500,
                        "msrp_aud_max": 72900,
                        "fuel_consumption_l_100km": 8.5,
                        "kerb_weight_kg": 1455,
                        "standard_features": ["18-inch S-design alloys", "quattro AWD", "Flat-bottom sports steering wheel", "Silk Nappa leather"],
                        "notes": "High-revving 188kW Australian benchmark."
                    },
                    {
                        "badge_name": "RS3 Sportback",
                        "years": {"start": 2012, "end": 2012},
                        "body_styles": ["5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic"],
                        "msrp_aud_min": 99900,
                        "msrp_aud_max": 105000,
                        "fuel_consumption_l_100km": 9.1,
                        "kerb_weight_kg": 1575,
                        "standard_features": ["19-inch Rotor alloys", "Carbon-fibre reinforced front fenders", "Brembo 4-piston front brakes", "quattro sport diff"],
                        "notes": "0-100km/h in 4.6s. Five-cylinder icon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "RS3 Sportback",
                        "body_style": "5-door Sportback",
                        "engine_code": "CEPA",
                        "transmission": "7-speed S tronic",
                        "drivetrain": "AWD",
                        "years_start": 2012,
                        "years_end": 2012,
                        "msrp_aud": 99900,
                        "power_kw": 250,
                        "torque_nm": 450,
                        "fuel_l_100km": 9.1,
                        "towing_braked_kg": 1500,
                        "notes": "First generation 250kW 5-cylinder RS3 Sportback."
                    }
                ]
            },
            {
                "series_code": "8V",
                "generation_name": "A3, S3 & RS3 Third Generation (Typ 8V)",
                "years": {"start": 2012, "end": 2020},
                "body_styles": ["5-door Sportback", "4-door Sedan", "Cabriolet"],
                "platform": "Volkswagen Group MQB",
                "ancap_rating": "5 stars",
                "summary": "Built on the MQB platform, introducing the wildly popular A3/S3/RS3 Sedan body style. S3 delivered 206kW-228kW, while the RS3 featured the all-aluminium DAZA 2.5L five-cylinder pumping out 294kW and 480Nm.",
                "engines": [
                    {
                        "engine_code": "CJXB/DJHA",
                        "name": "2.0L TFSI Turbo Petrol (S3)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 213,
                        "power_rpm": "5400-6500",
                        "torque_nm": 380,
                        "torque_rpm": "1850-5300",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Australian hot-climate spec 206kW up to 213kW/228kW."
                    },
                    {
                        "engine_code": "DAZA",
                        "name": "2.5L TFSI 5-Cylinder Turbo (RS3)",
                        "displacement_cc": 2480,
                        "displacement_litres": 2.5,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 294,
                        "power_rpm": "5850-7000",
                        "torque_nm": 480,
                        "torque_rpm": "1700-5850",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 20-valve",
                        "notes": "All-aluminium crankcase saving 26kg; 400hp Five-Cylinder powerhouse."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "S3 Sedan / Sportback",
                        "years": {"start": 2013, "end": 2020},
                        "body_styles": ["4-door Sedan", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed S tronic", "7-speed S tronic"],
                        "msrp_aud_min": 59990,
                        "msrp_aud_max": 65800,
                        "fuel_consumption_l_100km": 6.9,
                        "kerb_weight_kg": 1445,
                        "standard_features": ["Virtual Cockpit display", "quattro AWD", "18-inch alloys", "Nappa sports seats", "Audi magnetic ride"],
                        "notes": "One of Australia's top-selling performance sedans."
                    },
                    {
                        "badge_name": "RS3 Sedan / Sportback",
                        "years": {"start": 2015, "end": 2020},
                        "body_styles": ["4-door Sedan", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic"],
                        "msrp_aud_min": 78900,
                        "msrp_aud_max": 86500,
                        "fuel_consumption_l_100km": 8.4,
                        "kerb_weight_kg": 1515,
                        "standard_features": ["19-inch Blade alloys", "RS sports exhaust with oval tips", "8-piston front brakes with wave discs", "Virtual Cockpit with RS screens"],
                        "notes": "0-100km/h in 4.1s. Modern performance legend."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "RS3 Sedan / Sportback",
                        "body_style": "4-door Sedan",
                        "engine_code": "DAZA",
                        "transmission": "7-speed S tronic",
                        "drivetrain": "AWD",
                        "years_start": 2017,
                        "years_end": 2020,
                        "msrp_aud": 84900,
                        "power_kw": 294,
                        "torque_nm": 480,
                        "fuel_l_100km": 8.4,
                        "towing_braked_kg": 1600,
                        "notes": "294kW 400hp all-aluminium 5-cylinder RS3 sedan."
                    }
                ]
            },
            {
                "series_code": "8Y",
                "generation_name": "A3, S3 & RS3 Fourth Generation (Typ 8Y)",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["5-door Sportback", "4-door Sedan"],
                "platform": "Volkswagen Group MQB evo",
                "ancap_rating": "5 stars",
                "summary": "Built on MQB evo with sharp polygonal styling. Features the 228kW S3 and the flagship RS3 armed with 294kW, 500Nm, and the revolutionary RS Torque Splitter rear differential with RS Torque Rear drift mode.",
                "engines": [
                    {
                        "engine_code": "DNFB",
                        "name": "2.0L TFSI Turbo Petrol (S3)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 228,
                        "power_rpm": "5450-6500",
                        "torque_nm": 400,
                        "torque_rpm": "2000-5450",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "EA888 evo4 high-output powertrain."
                    },
                    {
                        "engine_code": "DNWA",
                        "name": "2.5L TFSI 5-Cylinder Turbo (RS3)",
                        "displacement_cc": 2480,
                        "displacement_litres": 2.5,
                        "cylinders": 5,
                        "configuration": "Inline-5",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 294,
                        "power_rpm": "5600-7000",
                        "torque_nm": 500,
                        "torque_rpm": "2250-5600",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 20-valve",
                        "notes": "500Nm torque output; paired with dual multi-plate clutch RS Torque Splitter."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "S3 Sedan / Sportback",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["4-door Sedan", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic"],
                        "msrp_aud_min": 70700,
                        "msrp_aud_max": 73200,
                        "fuel_consumption_l_100km": 7.4,
                        "kerb_weight_kg": 1500,
                        "standard_features": ["19-inch 5-arm alloys", "Matrix LED headlights", "Audi Virtual Cockpit Plus", "quattro AWD"],
                        "notes": "0-100km/h in 4.8 seconds."
                    },
                    {
                        "badge_name": "RS3 Sedan / Sportback",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["4-door Sedan", "5-door Sportback"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed S tronic"],
                        "msrp_aud_min": 91400,
                        "msrp_aud_max": 96900,
                        "fuel_consumption_l_100km": 8.3,
                        "kerb_weight_kg": 1570,
                        "standard_features": ["RS Torque Splitter with drift mode", "19-inch graphic RS alloys", "Matrix LED headlights with checkered-flag animation", "RS sport seats in Fine Nappa leather"],
                        "notes": "0-100km/h in 3.8s. Nurburgring compact lap record holder."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "RS3 Sedan / Sportback",
                        "body_style": "4-door Sedan",
                        "engine_code": "DNWA",
                        "transmission": "7-speed S tronic",
                        "drivetrain": "AWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 93900,
                        "power_kw": 294,
                        "torque_nm": 500,
                        "fuel_l_100km": 8.3,
                        "towing_braked_kg": 1600,
                        "notes": "500Nm RS Torque Splitter drift-capable 5-cylinder sedan."
                    }
                ]
            }
        ]
    }
}
