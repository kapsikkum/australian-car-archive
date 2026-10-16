"""
Deep-dive models 1 to 7 for Australian Car Archive Group 3
"""
from typing import Dict, Any

DEEP_DIVE_MODELS_PART1: Dict[str, Dict[str, Any]] = {
    "volkswagen/golf": {
        "make_slug": "volkswagen",
        "model_slug": "golf",
        "name": "Golf",
        "vehicle_type": "Hatchback / Wagon",
        "segment": "Small Car",
        "years_sold_au": {"start": 1976, "end": "Present"},
        "locally_built": True,
        "assembly_plants_au": ["Clayton, Victoria (1976-1982)"],
        "overview": "The benchmark European hatchback in Australia across eight generations. The Golf introduced front-wheel drive hatchback dynamics to Australia, initially assembled locally at Clayton, Victoria, and evolved into Australia's favorite hot hatchback through the legendary Golf GTI and all-wheel-drive Golf R.",
        "australian_market_notes": "First assembled at Clayton, Victoria in 1976 with 1.6-litre petrol and 1.5-litre diesel engines. The Golf GTI was formally introduced in 1990 (Mk2) and took off rapidly in Mk4 and Mk5 eras, with Australia becoming one of the top per-capita markets for the GTI and Golf R globally.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Mk1",
                "generation_name": "Golf Mark 1 (Typ 17)",
                "years": {"start": 1976, "end": 1982},
                "body_styles": ["3-door hatchback", "5-door hatchback"],
                "platform": "Volkswagen Group A1",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Assembled locally at Clayton, Victoria by Motor Producers Limited. Transformed the Australian market from rear-wheel drive sedans to front-wheel drive hatchback packaging.",
                "engines": [
                    {
                        "engine_code": "FP",
                        "name": "1.6L SOHC Petrol",
                        "displacement_cc": 1588,
                        "displacement_litres": 1.6,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 55,
                        "power_rpm": "5600",
                        "torque_nm": 117,
                        "torque_rpm": "3200",
                        "compression_ratio": "8.2:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "Single Solex carburettor tuned for Australian regular unleaded/leaded fuel."
                    },
                    {
                        "engine_code": "CK",
                        "name": "1.5L Diesel",
                        "displacement_cc": 1471,
                        "displacement_litres": 1.5,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Diesel",
                        "power_kw": 37,
                        "power_rpm": "5000",
                        "torque_nm": 80,
                        "torque_rpm": "3000",
                        "compression_ratio": "23.5:1",
                        "valvetrain": "SOHC 8-valve",
                        "notes": "One of the earliest passenger car diesel offerings in Australia, achieving sub-5.0L/100km economy."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "GLS 1.6",
                        "years": {"start": 1976, "end": 1982},
                        "body_styles": ["3-door hatchback", "5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["4-speed manual", "3-speed automatic"],
                        "msrp_aud_min": 4995,
                        "msrp_aud_max": 7250,
                        "fuel_consumption_l_100km": 7.8,
                        "kerb_weight_kg": 850,
                        "standard_features": ["Cloth trim", "Heated rear window", "Brake booster", "Reclining front seats"],
                        "notes": "Clayton-assembled top-trim launch model."
                    },
                    {
                        "badge_name": "GL Diesel",
                        "years": {"start": 1979, "end": 1982},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 6890,
                        "msrp_aud_max": 7990,
                        "fuel_consumption_l_100km": 5.2,
                        "kerb_weight_kg": 875,
                        "standard_features": ["Glow plug indicator", "High-economy gearing", "Tinted glass"],
                        "notes": "Economy leader during the late 70s oil crises."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "GLS 1.6",
                        "body_style": "5-door hatchback",
                        "engine_code": "FP",
                        "transmission": "4-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1976,
                        "years_end": "1982",
                        "msrp_aud": 5495,
                        "power_kw": 55,
                        "torque_nm": 117,
                        "fuel_l_100km": 7.8,
                        "towing_braked_kg": 800,
                        "notes": "Australian local production run."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Mk5",
                "generation_name": "Golf Mark 5 (Typ 1K)",
                "years": {"start": 2004, "end": 2009},
                "body_styles": ["5-door hatchback"],
                "platform": "Volkswagen Group PQ35",
                "ancap_rating": "5 stars",
                "summary": "Transformed the Golf with multi-link rear suspension, high structural rigidity, 6-speed DSG dual-clutch transmission, and ignited the modern Australian Golf GTI phenomenon.",
                "engines": [
                    {
                        "engine_code": "AXX/BWA",
                        "name": "2.0L Turbo FSI (GTI)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 147,
                        "power_rpm": "5100-6000",
                        "torque_nm": 280,
                        "torque_rpm": "1800-5000",
                        "compression_ratio": "10.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Direct injection turbo engine; defined modern hot hatch drivability."
                    },
                    {
                        "engine_code": "BUB",
                        "name": "3.2L VR6 (R32)",
                        "displacement_cc": 3189,
                        "displacement_litres": 3.2,
                        "cylinders": 6,
                        "configuration": "VR6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 184,
                        "power_rpm": "6300",
                        "torque_nm": 320,
                        "torque_rpm": "2500-3000",
                        "compression_ratio": "10.9:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Narrow-angle VR6 with Haldex 4Motion all-wheel drive and dual centre exhaust."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "GTI",
                        "years": {"start": 2005, "end": 2009},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "6-speed DSG"],
                        "msrp_aud_min": 39990,
                        "msrp_aud_max": 44990,
                        "fuel_consumption_l_100km": 8.0,
                        "kerb_weight_kg": 1360,
                        "standard_features": ["Interlagos tartan sports seats", "Flat-bottom leather steering wheel", "17-inch Denver alloys", "Bi-xenon headlights", "Dual-zone climate control"],
                        "notes": "Massive Australian sales hit, establishing a multi-month waiting list upon release."
                    },
                    {
                        "badge_name": "R32",
                        "years": {"start": 2006, "end": 2009},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual", "6-speed DSG"],
                        "msrp_aud_min": 54990,
                        "msrp_aud_max": 59990,
                        "fuel_consumption_l_100km": 10.7,
                        "kerb_weight_kg": 1530,
                        "standard_features": ["Haldex 4Motion AWD", "18-inch Zolder multi-spoke wheels", "Centre-exit twin exhausts", "Brushed aluminium grille", "Recaro bucket seats"],
                        "notes": "Cult naturally aspirated halo hot hatch."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "GTI",
                        "body_style": "5-door hatchback",
                        "engine_code": "AXX/BWA",
                        "transmission": "6-speed DSG",
                        "drivetrain": "FWD",
                        "years_start": 2005,
                        "years_end": "2009",
                        "msrp_aud": 42290,
                        "power_kw": 147,
                        "torque_nm": 280,
                        "fuel_l_100km": 8.0,
                        "towing_braked_kg": 1400,
                        "notes": "Flagship hot hatch with launch control."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Mk7",
                "generation_name": "Golf Mark 7 & 7.5 (Typ 5G)",
                "years": {"start": 2013, "end": "2020"},
                "body_styles": ["5-door hatchback", "Wagon"],
                "platform": "Volkswagen Group MQB",
                "ancap_rating": "5 stars",
                "summary": "MQB platform pioneer; lighter, stiffer, and technologically superior, winning 2013 Wheels Car of the Year. Spanned 90TSI/110TSI, 162kW-180kW GTI, and the 213kW Golf R.",
                "engines": [
                    {
                        "engine_code": "EA888 Gen 3",
                        "name": "2.0L TSI (GTI / Golf R)",
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
                        "compression_ratio": "9.6:1",
                        "valvetrain": "DOHC 16-valve, variable valve timing & lift",
                        "notes": "Golf R tune with reinforced block, larger turbocharger, and intercooler."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "GTI",
                        "years": {"start": 2013, "end": 2020},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "6-speed DSG", "7-speed DSG"],
                        "msrp_aud_min": 41990,
                        "msrp_aud_max": 47990,
                        "fuel_consumption_l_100km": 6.6,
                        "kerb_weight_kg": 1350,
                        "standard_features": ["Clark tartan seats", "VAQ electronically controlled mechanical front diff lock", "Adaptive Chassis Control (DCC)", "8.0-inch/9.2-inch touchscreen with Apple CarPlay"],
                        "notes": "162kW (Mk7) up to 180kW (Mk7.5 Performance) with 7-speed wet-clutch DSG."
                    },
                    {
                        "badge_name": "R",
                        "years": {"start": 2014, "end": 2020},
                        "body_styles": ["5-door hatchback", "Wagon"],
                        "drivetrain": "AWD",
                        "transmissions": ["6-speed manual", "6-speed DSG", "7-speed DSG"],
                        "msrp_aud_min": 51990,
                        "msrp_aud_max": 59990,
                        "fuel_consumption_l_100km": 7.3,
                        "kerb_weight_kg": 1450,
                        "standard_features": ["4Motion all-wheel drive", "Quad exhaust outlets", "Pretoria 19-inch alloys", "Digital Cockpit virtual instrument cluster"],
                        "notes": "Top-selling performance all-rounder in Australia, capable of 0-100 km/h in 4.8 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "R",
                        "body_style": "5-door hatchback",
                        "engine_code": "EA888 Gen 3",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2017,
                        "years_end": "2020",
                        "msrp_aud": 55990,
                        "power_kw": 213,
                        "torque_nm": 380,
                        "fuel_l_100km": 7.2,
                        "towing_braked_kg": 0,
                        "notes": "Mk7.5 facelift with full digital cockpit and Pretoria alloys."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Mk8",
                "generation_name": "Golf Mark 8 & 8.5 (Typ CD1)",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["5-door hatchback", "Wagon"],
                "platform": "Volkswagen Group MQB Evo",
                "ancap_rating": "5 stars",
                "summary": "Digitized cockpit, shift-by-wire controls, IQ.LIGHT LED matrix lighting, 180kW GTI, and 235kW Golf R with rear torque-vectoring drift mode.",
                "engines": [
                    {
                        "engine_code": "EA888 Gen 4",
                        "name": "2.0L TSI (Golf R)",
                        "displacement_cc": 1984,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 235,
                        "power_rpm": "5200-6500",
                        "torque_nm": 400,
                        "torque_rpm": "2000-5600",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "350-bar direct fuel injection; features R-Performance Torque Vectoring."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "GTI",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["5-door hatchback"],
                        "drivetrain": "FWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 53300,
                        "msrp_aud_max": 56900,
                        "fuel_consumption_l_100km": 7.0,
                        "kerb_weight_kg": 1409,
                        "standard_features": ["18-inch Richmond alloys", "Innovision Cockpit", "DCC Adaptive Damping", "Scale Paper tartan seats", "LED light bar in grille"],
                        "notes": "180kW/370Nm hot hatch flagship."
                    },
                    {
                        "badge_name": "R",
                        "years": {"start": 2022, "end": "Present"},
                        "body_styles": ["5-door hatchback", "Wagon"],
                        "drivetrain": "AWD",
                        "transmissions": ["7-speed DSG"],
                        "msrp_aud_min": 68990,
                        "msrp_aud_max": 71990,
                        "fuel_consumption_l_100km": 7.8,
                        "kerb_weight_kg": 1514,
                        "standard_features": ["Torque Vectoring 4Motion", "Drift and Special (Nurburgring) drive modes", "19-inch Estoril alloys", "Nappa leather bucket seats", "Harman Kardon premium audio"],
                        "notes": "0-100 km/h in 4.7 seconds with R-Performance package standard in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "R",
                        "body_style": "5-door hatchback",
                        "engine_code": "EA888 Gen 4",
                        "transmission": "7-speed DSG",
                        "drivetrain": "AWD",
                        "years_start": 2022,
                        "years_end": "Present",
                        "msrp_aud": 68990,
                        "power_kw": 235,
                        "torque_nm": 400,
                        "fuel_l_100km": 7.8,
                        "towing_braked_kg": 1700,
                        "notes": "Features twin-clutch rear torque vectoring."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "volkswagen/amarok": {
        "make_slug": "volkswagen",
        "model_slug": "amarok",
        "name": "Amarok",
        "vehicle_type": "Ute / Pickup Truck",
        "segment": "Mid-size Dual-Cab Ute",
        "years_sold_au": {"start": 2011, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Volkswagen's rugged mid-size commercial pickup truck, celebrated in Australia for full-time 4Motion all-wheel drive, class-leading tub width capable of carrying a full-sized Australian pallet between the wheel arches, and powerhouse 3.0-litre V6 TDI engines developed with Walkinshaw Automotive (W580).",
        "australian_market_notes": "First arrived in 2011 with 2.0-litre bi-turbo diesel engines. Revolutionized the Australian ute market in 2016 with the introduction of the 3.0-litre V6 TDI (up to 200kW on overboost), offering car-like refinement and permanent AWD. The second generation (2023+) was co-developed with Ford on the updated T6 platform, retaining distinct Volkswagen steering, interior, and suspension tuning.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "2H",
                "generation_name": "Amarok First Generation",
                "years": {"start": 2011, "end": 2022},
                "body_styles": ["Dual-cab ute", "Single-cab ute"],
                "platform": "Volkswagen Group 2H",
                "ancap_rating": "5 stars",
                "summary": "Original German-designed ladder-frame ute, offering 2.0 Bi-TDI and legendary 3.0 V6 TDI with permanent 4Motion and Walkinshaw W580 tuning.",
                "engines": [
                    {
                        "engine_code": "EA189 BiTDI",
                        "name": "2.0L Bi-Turbo Diesel",
                        "displacement_cc": 1968,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 132,
                        "power_rpm": "4000",
                        "torque_nm": 420,
                        "torque_rpm": "1500-2000",
                        "compression_ratio": "16.5:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Sequentially turbocharged common-rail diesel."
                    },
                    {
                        "engine_code": "EA897 V6 TDI",
                        "name": "3.0L V6 Turbo Diesel",
                        "displacement_cc": 2967,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 190,
                        "power_rpm": "3250-4500",
                        "torque_nm": 580,
                        "torque_rpm": "1400-3000",
                        "compression_ratio": "17.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "200kW overboost in Highline/Ultimate and W580 Walkinshaw editions."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "TDI580 Highline",
                        "years": {"start": 2018, "end": 2022},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 61990,
                        "msrp_aud_max": 65990,
                        "fuel_consumption_l_100km": 8.9,
                        "kerb_weight_kg": 2150,
                        "standard_features": ["Permanent 4Motion", "18-inch Rawson alloys", "Bi-xenon headlights", "Rear mechanical diff lock", "Apple CarPlay & Android Auto", "3500kg tow pack"],
                        "notes": "Australia's top-selling V6 Amarok variant."
                    },
                    {
                        "badge_name": "W580S (Walkinshaw)",
                        "years": {"start": 2021, "end": 2022},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed automatic"],
                        "msrp_aud_min": 79990,
                        "msrp_aud_max": 82990,
                        "fuel_consumption_l_100km": 9.5,
                        "kerb_weight_kg": 2190,
                        "standard_features": ["Walkinshaw-tuned MTV twin-tube dampers", "20-inch forged Clayton alloy wheels", "Twin side-exit exhaust", "Bespoke sports bar and decal package", "Vienna leather interior"],
                        "notes": "Developed and assembled in Clayton, Victoria by Walkinshaw Automotive."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "TDI580 Highline",
                        "body_style": "Dual-cab ute",
                        "engine_code": "EA897 V6 TDI",
                        "transmission": "8-speed automatic",
                        "drivetrain": "AWD",
                        "years_start": 2018,
                        "years_end": "2022",
                        "msrp_aud": 61990,
                        "power_kw": 190,
                        "torque_nm": 580,
                        "fuel_l_100km": 8.9,
                        "towing_braked_kg": 3500,
                        "notes": "Permanent AWD with rear differential lock."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "T1",
                "generation_name": "Amarok Second Generation (Next-Gen)",
                "years": {"start": 2023, "end": "Present"},
                "body_styles": ["Dual-cab ute"],
                "platform": "Ford/VW T6.2 platform",
                "ancap_rating": "5 stars",
                "summary": "Next-Gen Amarok co-developed with Ford, featuring Core, Life, Style, PanAmericana, and Aventura trims with 3.0L V6 TDI (184kW/600Nm) and 2.3L TSI turbo petrol (222kW).",
                "engines": [
                    {
                        "engine_code": "Power Stroke 3.0 V6",
                        "name": "3.0L V6 Turbo Diesel",
                        "displacement_cc": 2993,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "V6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 184,
                        "power_rpm": "3250",
                        "torque_nm": 600,
                        "torque_rpm": "1750-2250",
                        "compression_ratio": "16.0:1",
                        "valvetrain": "DOHC 24-valve",
                        "notes": "Paired with 10-speed automatic and 4A permanent all-wheel drive."
                    },
                    {
                        "engine_code": "EcoBoost 2.3 TSI",
                        "name": "2.3L Turbo Petrol",
                        "displacement_cc": 2261,
                        "displacement_litres": 2.3,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 222,
                        "power_rpm": "5900",
                        "torque_nm": 452,
                        "torque_rpm": "3350",
                        "compression_ratio": "10.0:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Exclusive to the flagship Amarok Aventura."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "PanAmericana V6",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "4WD",
                        "transmissions": ["10-speed automatic"],
                        "msrp_aud_min": 75990,
                        "msrp_aud_max": 78990,
                        "fuel_consumption_l_100km": 8.4,
                        "kerb_weight_kg": 2240,
                        "standard_features": ["Matte black exterior trim", "18-inch black alloys with all-terrain tyres", "12-inch vertical infotainment screen", "Harmon Kardon 8-speaker sound", "Spray-in bedliner", "IQ.Light matrix LEDs"],
                        "notes": "Off-road luxury flagship with 3.0L V6 TDI."
                    },
                    {
                        "badge_name": "Aventura V6",
                        "years": {"start": 2023, "end": "Present"},
                        "body_styles": ["Dual-cab ute"],
                        "drivetrain": "4WD",
                        "transmissions": ["10-speed automatic"],
                        "msrp_aud_min": 79990,
                        "msrp_aud_max": 82990,
                        "fuel_consumption_l_100km": 8.4,
                        "kerb_weight_kg": 2280,
                        "standard_features": ["21-inch alloy wheels", "Chrome exterior accents", "Electric roll cover", "Savona leather upholstery", "Park Assist Plus"],
                        "notes": "Top-tier highway touring luxury."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "PanAmericana V6",
                        "body_style": "Dual-cab ute",
                        "engine_code": "Power Stroke 3.0 V6",
                        "transmission": "10-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2023,
                        "years_end": "Present",
                        "msrp_aud": 75990,
                        "power_kw": 184,
                        "torque_nm": 600,
                        "fuel_l_100km": 8.4,
                        "towing_braked_kg": 3500,
                        "notes": "Rugged off-road styling with dual-range full-time 4WD."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "bmw/3-series": {
        "make_slug": "bmw",
        "model_slug": "3-series",
        "name": "3 Series",
        "vehicle_type": "Sedan / Coupe / Wagon / Convertible",
        "segment": "Medium Luxury Sports Car",
        "years_sold_au": {"start": 1976, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "The benchmark executive sports sedan in Australia across seven distinct generations: E21, E30, E36, E46, E90, F30, and G20. Revered for near-perfect 50:50 weight distribution, rear-wheel drive chassis balance, silky inline-six engines, and iconic M3 motorsport heroes.",
        "australian_market_notes": "First sold in Australia in 1976 (E21 318 and 320). In 1987, Jim Richards and Tony Longhurst drove the E30 M3 to Australian Touring Car Championship dominance, firmly lodging the 3 Series in Australian car culture. Australia remains one of BMW's strongest global markets for the 3 Series and M3.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "E30",
                "generation_name": "3 Series E30",
                "years": {"start": 1983, "end": 1991},
                "body_styles": ["2-door sedan", "4-door sedan", "Convertible", "Touring"],
                "platform": "BMW E30",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The defining cult compact BMW; 318i, 323i, 325i, and Group A homologation M3 with S14 2.3L twin-cam four.",
                "engines": [
                    {
                        "engine_code": "M20B25",
                        "name": "2.5L SOHC Inline-6",
                        "displacement_cc": 2494,
                        "displacement_litres": 2.5,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 125,
                        "power_rpm": "5800",
                        "torque_nm": 226,
                        "torque_rpm": "4000",
                        "compression_ratio": "8.8:1",
                        "valvetrain": "SOHC 12-valve",
                        "notes": "Bosch Motronic injection, standard on Australian 325i."
                    },
                    {
                        "engine_code": "S14B23",
                        "name": "2.3L DOHC M-Power (M3)",
                        "displacement_cc": 2302,
                        "displacement_litres": 2.3,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 147,
                        "power_rpm": "6750",
                        "torque_nm": 240,
                        "torque_rpm": "4750",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 16-valve, individual throttle bodies",
                        "notes": "Group A touring car homologation powerplant."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "325i",
                        "years": {"start": 1986, "end": 1991},
                        "body_styles": ["2-door sedan", "4-door sedan", "Convertible"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual", "4-speed automatic"],
                        "msrp_aud_min": 56900,
                        "msrp_aud_max": 75900,
                        "fuel_consumption_l_100km": 9.2,
                        "kerb_weight_kg": 1180,
                        "standard_features": ["Four-wheel disc brakes with ABS", "Limited-slip differential (optional/sport)", "Power steering", "Air conditioning", "14-inch basketweave alloys"],
                        "notes": "Benchmark sports sedan of the late 1980s."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "325i",
                        "body_style": "2-door sedan",
                        "engine_code": "M20B25",
                        "transmission": "5-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1986,
                        "years_end": "1991",
                        "msrp_aud": 58900,
                        "power_kw": 125,
                        "torque_nm": 226,
                        "fuel_l_100km": 9.2,
                        "towing_braked_kg": 1200,
                        "notes": "Classic sport manual specification."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "E46",
                "generation_name": "3 Series E46",
                "years": {"start": 1998, "end": 2006},
                "body_styles": ["4-door sedan", "2-door coupe", "Convertible", "Touring wagon", "Compact"],
                "platform": "BMW E46",
                "ancap_rating": "4 stars",
                "summary": "Universally acclaimed for timeless styling, aluminum suspension components, 318i to 330i, and the revered 252kW S54 M3 and lightweight M3 CSL.",
                "engines": [
                    {
                        "engine_code": "M54B30",
                        "name": "3.0L DOHC Inline-6",
                        "displacement_cc": 2979,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 170,
                        "power_rpm": "5900",
                        "torque_nm": 300,
                        "torque_rpm": "3500",
                        "compression_ratio": "10.2:1",
                        "valvetrain": "DOHC 24-valve, Double-VANOS",
                        "notes": "Silky, linear power delivery on 330i and 330Ci."
                    },
                    {
                        "engine_code": "S54B32",
                        "name": "3.2L DOHC M-Power (M3)",
                        "displacement_cc": 3246,
                        "displacement_litres": 3.2,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 252,
                        "power_rpm": "7900",
                        "torque_nm": 365,
                        "torque_rpm": "4900",
                        "compression_ratio": "11.5:1",
                        "valvetrain": "DOHC 24-valve, 6 individual throttles, Double-VANOS",
                        "notes": "8,000rpm redline; widely considered one of the greatest naturally aspirated engines ever built."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "330Ci",
                        "years": {"start": 2000, "end": 2006},
                        "body_styles": ["2-door coupe", "Convertible"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual", "6-speed manual", "5-speed Steptronic automatic"],
                        "msrp_aud_min": 89900,
                        "msrp_aud_max": 99900,
                        "fuel_consumption_l_100km": 9.1,
                        "kerb_weight_kg": 1430,
                        "standard_features": ["M Aerodynamic pack", "17-inch/18-inch M double-spoke wheels", "Harman Kardon audio", "Dynamic Stability Control (DSC)", "Memory sports seats"],
                        "notes": "Flagship non-M coupe."
                    },
                    {
                        "badge_name": "M3",
                        "years": {"start": 2001, "end": 2006},
                        "body_styles": ["2-door coupe", "Convertible"],
                        "drivetrain": "RWD",
                        "transmissions": ["6-speed manual", "6-speed SMG-II automated manual"],
                        "msrp_aud_min": 142000,
                        "msrp_aud_max": 162000,
                        "fuel_consumption_l_100km": 11.9,
                        "kerb_weight_kg": 1495,
                        "standard_features": ["Variable M Differential Lock", "19-inch forged alloy wheels", "Quad chrome exhaust tips", "Power-dome aluminium bonnet", "Wider wheel flares"],
                        "notes": "Australian performance icon; 0-100 km/h in 5.2 seconds."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M3",
                        "body_style": "2-door coupe",
                        "engine_code": "S54B32",
                        "transmission": "6-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 2001,
                        "years_end": "2006",
                        "msrp_aud": 142000,
                        "power_kw": 252,
                        "torque_nm": 365,
                        "fuel_l_100km": 11.9,
                        "towing_braked_kg": 0,
                        "notes": "Traditional 6-speed Getrag manual coupe."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "G20",
                "generation_name": "3 Series G20",
                "years": {"start": 2019, "end": "Present"},
                "body_styles": ["4-door sedan", "Touring wagon"],
                "platform": "BMW CLAR platform",
                "ancap_rating": "5 stars",
                "summary": "Stiffer CLAR platform, 320i, 330i, M340i xDrive (285kW B58), and G80 M3 (up to 375kW Competition and 405kW CS), introducing the first-ever M3 Touring wagon.",
                "engines": [
                    {
                        "engine_code": "B58B30",
                        "name": "3.0L TwinPower Turbo Inline-6",
                        "displacement_cc": 2998,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 285,
                        "power_rpm": "5800-6500",
                        "torque_nm": 500,
                        "torque_rpm": "1800-5000",
                        "compression_ratio": "10.2:1",
                        "valvetrain": "DOHC 24-valve, Valvetronic & Double-VANOS",
                        "notes": "Twin-scroll turbocharger with water-to-air intercooling in M340i xDrive."
                    },
                    {
                        "engine_code": "S58B30",
                        "name": "3.0L Twin-Turbo M-Power (M3 Competition)",
                        "displacement_cc": 2993,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 375,
                        "power_rpm": "6250",
                        "torque_nm": 650,
                        "torque_rpm": "2750-5500",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 24-valve, 3D-printed cylinder head core",
                        "notes": "Powers G80 M3 Competition sedan and G81 M3 Touring."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "M340i xDrive",
                        "years": {"start": 2019, "end": "Present"},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "AWD",
                        "transmissions": ["8-speed sport automatic"],
                        "msrp_aud_min": 99900,
                        "msrp_aud_max": 106200,
                        "fuel_consumption_l_100km": 7.7,
                        "kerb_weight_kg": 1670,
                        "standard_features": ["M Sport differential", "Adaptive M suspension", "19-inch M alloy wheels", "BMW Laserlight / Matrix LED", "Harman Kardon sound", "BMW Curved Display"],
                        "notes": "0-100 km/h in 4.4 seconds with rear-biased AWD."
                    },
                    {
                        "badge_name": "M3 Competition",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["4-door sedan", "Touring wagon"],
                        "drivetrain": "RWD / AWD (M xDrive)",
                        "transmissions": ["8-speed M Steptronic"],
                        "msrp_aud_min": 153500,
                        "msrp_aud_max": 178900,
                        "fuel_consumption_l_100km": 10.2,
                        "kerb_weight_kg": 1730,
                        "standard_features": ["Carbon-fibre roof", "Active M differential", "M Drive Professional with 10-stage traction control", "Carbon-ceramic brakes (optional)", "Merino leather interior"],
                        "notes": "0-100 km/h in 3.5 seconds (M xDrive)."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "M3 Competition",
                        "body_style": "4-door sedan",
                        "engine_code": "S58B30",
                        "transmission": "8-speed M Steptronic",
                        "drivetrain": "AWD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 169500,
                        "power_kw": 375,
                        "torque_nm": 650,
                        "fuel_l_100km": 10.2,
                        "towing_braked_kg": 0,
                        "notes": "M xDrive with 2WD rear-drive mode."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "mercedes-benz/c-class": {
        "make_slug": "mercedes-benz",
        "model_slug": "c-class",
        "name": "C-Class",
        "vehicle_type": "Sedan / Wagon / Coupe / Convertible",
        "segment": "Medium Luxury Car",
        "years_sold_au": {"start": 1994, "end": "Present"},
        "locally_built": False,
        "assembly_plants_au": [],
        "overview": "Mercedes-Benz's most popular luxury nameplate in Australia, spanning W202, W203, W204, W205, and W206. Renowned for supreme safety engineering, quiet cabin isolation, and thundering naturally aspirated and biturbo V8 AMG performance flagships.",
        "australian_market_notes": "Succeeded the legendary 190E (W201) in 1994. The C-Class held the title of Australia's best-selling luxury car for over a decade. Australia emerged as one of the world's most enthusiastic markets for AMG C-Class models, with the W204 C63 AMG (6.2L M156 V8) developing a massive cult following.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "W204",
                "generation_name": "C-Class W204",
                "years": {"start": 2007, "end": 2014},
                "body_styles": ["4-door sedan", "Estate wagon", "2-door coupe"],
                "platform": "Mercedes-Benz W204",
                "ancap_rating": "5 stars",
                "summary": "Agility Control damping, Classic/Elegance/Avantgarde styling divides, C200 CGI, C250, C300, and the legendary naturally aspirated 6.2L V8 C63 AMG.",
                "engines": [
                    {
                        "engine_code": "M271 EVO",
                        "name": "1.8L Turbo CGI",
                        "displacement_cc": 1796,
                        "displacement_litres": 1.8,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 150,
                        "power_rpm": "5500",
                        "torque_nm": 310,
                        "torque_rpm": "2000-4300",
                        "compression_ratio": "9.3:1",
                        "valvetrain": "DOHC 16-valve",
                        "notes": "Direct injection turbocharged four-cylinder in C250 CGI."
                    },
                    {
                        "engine_code": "M156",
                        "name": "6.2L Naturally Aspirated AMG V8",
                        "displacement_cc": 6208,
                        "displacement_litres": 6.2,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 336,
                        "power_rpm": "6800",
                        "torque_nm": 600,
                        "torque_rpm": "5000",
                        "compression_ratio": "11.3:1",
                        "valvetrain": "DOHC 32-valve, bucket tappets",
                        "notes": "Legendary AMG powerplant producing up to 373kW in Edition 507 and 380kW in Black Series."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "C250 Avantgarde",
                        "years": {"start": 2010, "end": 2014},
                        "body_styles": ["4-door sedan", "Estate wagon", "Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["7G-Tronic 7-speed automatic"],
                        "msrp_aud_min": 65900,
                        "msrp_aud_max": 71900,
                        "fuel_consumption_l_100km": 7.2,
                        "kerb_weight_kg": 1505,
                        "standard_features": ["Avantgarde sports grille with large tri-star", "18-inch alloy wheels", "COMAND navigation", "Artico leather upholstery", "Bi-xenon headlights"],
                        "notes": "Volume luxury sweet-spot in Australia."
                    },
                    {
                        "badge_name": "C63 AMG",
                        "years": {"start": 2008, "end": 2014},
                        "body_styles": ["4-door sedan", "Estate wagon", "Coupe"],
                        "drivetrain": "RWD",
                        "transmissions": ["AMG Speedshift Plus 7G-Tronic / MCT"],
                        "msrp_aud_min": 139900,
                        "msrp_aud_max": 169900,
                        "fuel_consumption_l_100km": 13.4,
                        "kerb_weight_kg": 1730,
                        "standard_features": ["6.2L V8", "Power-dome aluminium bonnet", "AMG high-performance composite brakes", "Nappa leather sports bucket seats", "Quad oval exhaust pipes"],
                        "notes": "Cult status in Australia; acclaimed for tyre-smoking V8 muscle and NASCAR-grade exhaust note."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "C63 AMG",
                        "body_style": "4-door sedan",
                        "engine_code": "M156",
                        "transmission": "AMG Speedshift Plus 7G-Tronic",
                        "drivetrain": "RWD",
                        "years_start": 2008,
                        "years_end": "2014",
                        "msrp_aud": 149900,
                        "power_kw": 336,
                        "torque_nm": 600,
                        "fuel_l_100km": 13.4,
                        "towing_braked_kg": 0,
                        "notes": "Naturally aspirated 6.2L V8 muscle sedan."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "W205",
                "generation_name": "C-Class W205",
                "years": {"start": 2014, "end": 2021},
                "body_styles": ["4-door sedan", "Estate wagon", "2-door coupe", "Convertible"],
                "platform": "Mercedes-Benz MRA platform",
                "ancap_rating": "5 stars",
                "summary": "MRA aluminium-hybrid lightweight architecture, S-Class inspired interior design, 3.0 V6 C43 AMG, and 375kW 4.0L Biturbo V8 C63 S.",
                "engines": [
                    {
                        "engine_code": "M177",
                        "name": "4.0L Biturbo AMG V8 (C63 S)",
                        "displacement_cc": 3982,
                        "displacement_litres": 4.0,
                        "cylinders": 8,
                        "configuration": "V8",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 375,
                        "power_rpm": "5500-6250",
                        "torque_nm": 700,
                        "torque_rpm": "1750-4500",
                        "compression_ratio": "10.5:1",
                        "valvetrain": "DOHC 32-valve, 'Hot inside V' turbochargers",
                        "notes": "Dry-sump-inspired engineering with twin turbos nestled between cylinder banks."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "C63 S AMG",
                        "years": {"start": 2015, "end": 2021},
                        "body_styles": ["4-door sedan", "Estate wagon", "Coupe", "Cabriolet"],
                        "drivetrain": "RWD",
                        "transmissions": ["AMG Speedshift MCT 7-speed / 9-speed"],
                        "msrp_aud_min": 154900,
                        "msrp_aud_max": 189900,
                        "fuel_consumption_l_100km": 8.6,
                        "kerb_weight_kg": 1655,
                        "standard_features": ["Electronic locking rear differential", "Dynamic engine mounts", "Burmester surround sound", "AMG Ride Control adaptive damping", "Performance exhaust with bypass flaps"],
                        "notes": "375kW/700Nm performance benchmark in Australia."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "C63 S AMG",
                        "body_style": "4-door sedan",
                        "engine_code": "M177",
                        "transmission": "AMG Speedshift MCT 7-speed",
                        "drivetrain": "RWD",
                        "years_start": 2015,
                        "years_end": "2021",
                        "msrp_aud": 154900,
                        "power_kw": 375,
                        "torque_nm": 700,
                        "fuel_l_100km": 8.6,
                        "towing_braked_kg": 0,
                        "notes": "V8 biturbo with 700Nm torque."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "land-rover/defender": {
        "make_slug": "land-rover",
        "model_slug": "defender",
        "name": "Defender",
        "vehicle_type": "4WD / Off-Road Utility",
        "segment": "Heavy Off-Road 4WD",
        "years_sold_au": {"start": 1949, "end": "Present"},
        "locally_built": True,
        "assembly_plants_au": ["Pressed Metal Corporation, Enfield NSW (1956-1982)", "JRA Moorebank NSW (1982-1994)"],
        "overview": "The immortal off-road master of the Australian bush and Australian Defence Force. Built and adapted locally with unique Australian military specifications (Project Perentie 4x4 and 6x6 with Isuzu 4BD1 3.9L engines), live-axle County 110s, and re-imagined for the 21st century as the ultra-capable, luxury L663 Defender.",
        "australian_market_notes": "Originally imported for the Snowy Mountains Scheme in 1949. Local assembly by Pressed Metal Corp and JRA in Sydney produced Australian-exclusive variants, notably the Australian Army Perentie 4x4 and 6x6. Civil models adopted the 300Tdi, 5-cylinder Td5, and Ford Puma 2.4/2.2 TDCi until original production concluded in 2016. The all-new aluminium D7x monocoque L663 launched in 2020.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Perentie",
                "generation_name": "Australian Army Perentie 4x4 & 6x6",
                "years": {"start": 1987, "end": 2013},
                "body_styles": ["4x4 Soft Top", "4x4 Survey", "6x6 Long Wheelbase", "6x6 Ambulance", "6x6 Long Range Patrol"],
                "platform": "JRA Heavy Duty Galvanised Chassis",
                "ancap_rating": "Military Specification",
                "summary": "Purpose-designed by Jaguar Rover Australia (JRA) at Moorebank, NSW for the Australian Army. Featured a hot-dip galvanised chassis, heavy-duty suspension, and bulletproof Isuzu 4BD1 3.9-litre diesel engines.",
                "engines": [
                    {
                        "engine_code": "4BD1",
                        "name": "Isuzu 3.9L Naturally Aspirated Diesel",
                        "displacement_cc": 3856,
                        "displacement_litres": 3.9,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Diesel",
                        "power_kw": 66,
                        "power_rpm": "3200",
                        "torque_nm": 245,
                        "torque_rpm": "1900",
                        "compression_ratio": "17.5:1",
                        "valvetrain": "OHV 8-valve, gear-driven camshaft",
                        "notes": "Direct injection industrial diesel, renowned for running in extreme heat and dust with zero electronics."
                    },
                    {
                        "engine_code": "4BD1T",
                        "name": "Isuzu 3.9L Turbo Diesel (6x6)",
                        "displacement_cc": 3856,
                        "displacement_litres": 3.9,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 90,
                        "power_rpm": "3000",
                        "torque_nm": 314,
                        "torque_rpm": "1800",
                        "compression_ratio": "17.0:1",
                        "valvetrain": "OHV 8-valve, Garrett turbocharger",
                        "notes": "Fitted to the Australian Army Perentie 6x6 with unique wide-track front axle and leaf-sprung bogie drive rear."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Perentie 4x4 GS",
                        "years": {"start": 1987, "end": 2013},
                        "body_styles": ["Soft Top 4x4", "Survey 4x4"],
                        "drivetrain": "4WD",
                        "transmissions": ["LT95 4-speed manual with vacuum-operated centre diff lock"],
                        "msrp_aud_min": 35000,
                        "msrp_aud_max": 45000,
                        "fuel_consumption_l_100km": 11.5,
                        "kerb_weight_kg": 2250,
                        "standard_features": ["Galvanised chassis", "Spare wheel mounted on passenger side chassis", "ROPS roll-over protection", "Dual fuel tanks (135L total)", "Blackout lighting switch"],
                        "notes": "Over 2,500 units served with Australian armed forces."
                    },
                    {
                        "badge_name": "Perentie 6x6 Patrol",
                        "years": {"start": 1989, "end": 2013},
                        "body_styles": ["6x6 Long Wheelbase", "6x6 Long Range Patrol Vehicle (LRPV)"],
                        "drivetrain": "6x6",
                        "transmissions": ["LT95A 4-speed manual with auxiliary splitter box"],
                        "msrp_aud_min": 65000,
                        "msrp_aud_max": 85000,
                        "fuel_consumption_l_100km": 14.8,
                        "kerb_weight_kg": 3650,
                        "standard_features": ["Full-time 6x6 with inter-axle diff locks", "Bogie rear leaf rocker suspension", "Turbocharged Isuzu 4BD1T", "Power steering", "Winch", "Heavy-duty PTO"],
                        "notes": "Unique Australian-designed 6x6 tactical military transport."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Perentie 4x4 GS",
                        "body_style": "Soft Top 4x4",
                        "engine_code": "4BD1",
                        "transmission": "LT95 4-speed manual",
                        "drivetrain": "4WD",
                        "years_start": 1987,
                        "years_end": "2013",
                        "msrp_aud": 38000,
                        "power_kw": 66,
                        "torque_nm": 245,
                        "fuel_l_100km": 11.5,
                        "towing_braked_kg": 2000,
                        "notes": "Moorebank NSW built military tactical 4WD."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "L663",
                "generation_name": "Defender Modern L663",
                "years": {"start": 2020, "end": "Present"},
                "body_styles": ["Defender 90 (3-door)", "Defender 110 (5-door)", "Defender 130 (8-seat)"],
                "platform": "Jaguar Land Rover D7x",
                "ancap_rating": "5 stars",
                "summary": "Monocoque architecture three times stiffer than body-on-frame, 900mm wading depth, Terrain Response 2, D300 Ingenium mild-hybrid diesel, and 386kW V8 flagship.",
                "engines": [
                    {
                        "engine_code": "D300 Ingenium",
                        "name": "3.0L Inline-6 Twin-Turbo Diesel MHEV",
                        "displacement_cc": 2996,
                        "displacement_litres": 3.0,
                        "cylinders": 6,
                        "configuration": "Inline-6",
                        "aspiration": "Twin-Turbocharged",
                        "fuel_type": "Diesel",
                        "power_kw": 221,
                        "power_rpm": "4000",
                        "torque_nm": 650,
                        "torque_rpm": "1500-2500",
                        "compression_ratio": "15.5:1",
                        "valvetrain": "DOHC 24-valve, 48V mild hybrid",
                        "notes": "Australia's volume powertrain choice for the modern Defender."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "110 D300 X-Dynamic SE",
                        "years": {"start": 2021, "end": "Present"},
                        "body_styles": ["5-door 4WD"],
                        "drivetrain": "4WD",
                        "transmissions": ["8-speed automatic with dual-range transfer case"],
                        "msrp_aud_min": 105900,
                        "msrp_aud_max": 115900,
                        "fuel_consumption_l_100km": 7.9,
                        "kerb_weight_kg": 2380,
                        "standard_features": ["Electronic air suspension", "Configurable Terrain Response 2", "11.4-inch Pivi Pro screen", "Wade Sensing", "ClearSight ground view cameras", "3500kg towing capacity"],
                        "notes": "Heart of the modern Australian Defender range."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "110 D300 X-Dynamic SE",
                        "body_style": "5-door 4WD",
                        "engine_code": "D300 Ingenium",
                        "transmission": "8-speed automatic",
                        "drivetrain": "4WD",
                        "years_start": 2021,
                        "years_end": "Present",
                        "msrp_aud": 108900,
                        "power_kw": 221,
                        "torque_nm": 650,
                        "fuel_l_100km": 7.9,
                        "towing_braked_kg": 3500,
                        "notes": "3500kg braked towing with electronic air suspension."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "mini/mini-classic-moke": {
        "make_slug": "mini",
        "model_slug": "mini-classic-moke",
        "name": "Classic Mini / Cooper / Moke",
        "vehicle_type": "Hatchback / Utility / Roadster",
        "segment": "Small / Micro Car",
        "years_sold_au": {"start": 1961, "end": "Present"},
        "locally_built": True,
        "assembly_plants_au": ["BMC Victoria Park / Zetland, Sydney NSW (1961-1981)"],
        "overview": "The full story of the Mini in Australia: manufactured in Sydney at BMC Zetland (with Australian-developed wind-up windows and quarter-vents), immortalized by outright victory in the 1966 Bathurst 500, transformed into the Australian-engineered Californian Moke, and reborn as the modern BMW MINI Cooper and John Cooper Works.",
        "australian_market_notes": "Australian Minis built at Zetland NSW featured heavy adaptations for Australian dust and heat. In 1966, Bob Holden and Rauno Aaltonen drove an Australian-built Cooper S to victory in the Bathurst 500, leading an unprecedented 1-2-3-4-5-6-7-8-9 finish in class. The open-top Mini Moke was produced at Zetland until 1981 and exported globally. Modern BMW MINI launched in Australia in 2002.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "Classic-Cooper-S",
                "generation_name": "Mini Cooper S (Zetland Mk I & II)",
                "years": {"start": 1965, "end": "1971"},
                "body_styles": ["2-door saloon"],
                "platform": "BMC ADO15",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Manufactured at Zetland, Sydney. Twin 1.25-inch or 1.5-inch SU carburettors, Hydrolastic suspension, and 1966 Bathurst 500 conqueror.",
                "engines": [
                    {
                        "engine_code": "A-Series 1275",
                        "name": "1275cc Cooper S Twin-Carb",
                        "displacement_cc": 1275,
                        "displacement_litres": 1.275,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 56,
                        "power_rpm": "5800",
                        "torque_nm": 107,
                        "torque_rpm": "3000",
                        "compression_ratio": "9.75:1",
                        "valvetrain": "OHV 8-valve, pushrod",
                        "notes": "Twin 1.25-inch SU HS2 carburettors, close-ratio 4-speed gearbox, dual fuel tanks."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Cooper S",
                        "years": {"start": 1965, "end": 1971},
                        "body_styles": ["2-door saloon"],
                        "drivetrain": "FWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 2280,
                        "msrp_aud_max": 2490,
                        "fuel_consumption_l_100km": 8.5,
                        "kerb_weight_kg": 640,
                        "standard_features": ["7.5-inch Cooper S front disc brakes", "Twin fuel tanks (45L total)", "Oil cooler", "Hydrolastic suspension", "Australian wind-up windows with quarter vents"],
                        "notes": "Australia's giant-killing touring car legend."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Cooper S",
                        "body_style": "2-door saloon",
                        "engine_code": "A-Series 1275",
                        "transmission": "4-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1965,
                        "years_end": "1971",
                        "msrp_aud": 2280,
                        "power_kw": 56,
                        "torque_nm": 107,
                        "fuel_l_100km": 8.5,
                        "towing_braked_kg": 400,
                        "notes": "Bathurst specification with dual fuel tanks."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "Californian-Moke",
                "generation_name": "Australian Mini Moke & Californian",
                "years": {"start": 1966, "end": "1981"},
                "body_styles": ["Open utility / recreational"],
                "platform": "BMC ADO15 / YDO15",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "Designed and manufactured at Zetland, Sydney. Evolved with 13-inch wheels, tubular nudge bars, denim trim, and high ground clearance into Australia's favourite surf car.",
                "engines": [
                    {
                        "engine_code": "A-Series 998/1275",
                        "name": "998cc & 1275cc A-Series",
                        "displacement_cc": 1275,
                        "displacement_litres": 1.275,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 43,
                        "power_rpm": "5250",
                        "torque_nm": 88,
                        "torque_rpm": "2500",
                        "compression_ratio": "8.8:1",
                        "valvetrain": "OHV 8-valve",
                        "notes": "Single SU carburettor, rubber cone suspension."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Californian 1275",
                        "years": {"start": 1977, "end": 1981},
                        "body_styles": ["Open utility"],
                        "drivetrain": "FWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 3690,
                        "msrp_aud_max": 4990,
                        "fuel_consumption_l_100km": 7.5,
                        "kerb_weight_kg": 670,
                        "standard_features": ["13-inch road wheels", "Tubular front and rear nudge bars", "Sun-top canopy", "Denim-look seat trim", "Rear bench seat"],
                        "notes": "Australian surf lifestyle icon."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Californian 1275",
                        "body_style": "Open utility",
                        "engine_code": "A-Series 998/1275",
                        "transmission": "4-speed manual",
                        "drivetrain": "FWD",
                        "years_start": 1977,
                        "years_end": "1981",
                        "msrp_aud": 4250,
                        "power_kw": 43,
                        "torque_nm": 88,
                        "fuel_l_100km": 7.5,
                        "towing_braked_kg": 400,
                        "notes": "Australian manufactured Californian."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "F56",
                "generation_name": "Modern MINI Cooper / JCW (F56)",
                "years": {"start": 2014, "end": "Present"},
                "body_styles": ["3-door hatch", "5-door hatch", "Convertible"],
                "platform": "BMW UKL1 platform",
                "ancap_rating": "4 stars",
                "summary": "Modern BMW engineering; 1.5T Cooper, 141kW 2.0T Cooper S, 170kW JCW, and limited-edition 225kW GP3.",
                "engines": [
                    {
                        "engine_code": "B48A20",
                        "name": "2.0L TwinPower Turbo Inline-4 (Cooper S)",
                        "displacement_cc": 1998,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Turbocharged",
                        "fuel_type": "Petrol",
                        "power_kw": 141,
                        "power_rpm": "4700-6000",
                        "torque_nm": 280,
                        "torque_rpm": "1250-4750",
                        "compression_ratio": "11.0:1",
                        "valvetrain": "DOHC 16-valve, Double-VANOS",
                        "notes": "Punchy hot hatch with twin-tailpipe exhaust."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "Cooper S",
                        "years": {"start": 2014, "end": "Present"},
                        "body_styles": ["3-door hatch", "5-door hatch"],
                        "drivetrain": "FWD",
                        "transmissions": ["6-speed manual", "7-speed dual-clutch Steptronic"],
                        "msrp_aud_min": 39990,
                        "msrp_aud_max": 51990,
                        "fuel_consumption_l_100km": 6.2,
                        "kerb_weight_kg": 1225,
                        "standard_features": ["Circular 8.8-inch central display with LED ring", "Mini Driving Modes (Sport/Mid/Green)", "17-inch Roulette alloys", "Union Jack LED tail-lights"],
                        "notes": "Go-kart handling feel."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "Cooper S",
                        "body_style": "3-door hatch",
                        "engine_code": "B48A20",
                        "transmission": "7-speed dual-clutch Steptronic",
                        "drivetrain": "FWD",
                        "years_start": 2018,
                        "years_end": "Present",
                        "msrp_aud": 43900,
                        "power_kw": 141,
                        "torque_nm": 280,
                        "fuel_l_100km": 6.2,
                        "towing_braked_kg": 0,
                        "notes": "3-door hatchback with dual-clutch transmission."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    },
    "peugeot/504-505": {
        "make_slug": "peugeot",
        "model_slug": "504-505",
        "name": "504 / 505",
        "vehicle_type": "Sedan / Wagon / Ute",
        "segment": "Large Family Car",
        "years_sold_au": {"start": 1969, "end": "1993"},
        "locally_built": True,
        "assembly_plants_au": ["Martin & King / Motor Producers Ltd, Clayton VIC (1969-1977)", "Renault Australia, Heidelberg VIC (1977-1986)"],
        "overview": "The legendary French workhorses assembled in Melbourne for almost two decades. Revered across Australia for soaking up horrific outback corrugations with long-travel independent suspension, victorious in the 1970 Ampol Trial, and winning 1970 Wheels Car of the Year.",
        "australian_market_notes": "The 504 was assembled at Clayton and later Heidelberg alongside Renaults. Australian versions featured reinforced suspension towers, heavy-duty dust sealing, and local trim. The 505 followed in 1980, assembled in Heidelberg until local manufacturing ceased in 1986, continuing as an import until 1993.",
        "manuals": [],
        "pictures": [],
        "generations": [
            {
                "series_code": "504",
                "generation_name": "Peugeot 504",
                "years": {"start": 1969, "end": "1983"},
                "body_styles": ["4-door sedan", "5-door wagon", "Coupe utility (ute)"],
                "platform": "Peugeot 504",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "1970 Wheels Car of the Year; four-wheel independent suspension, torque-tube drive, four-wheel disc brakes, and rugged rally durability.",
                "engines": [
                    {
                        "engine_code": "XN1",
                        "name": "2.0L Carburettor Petrol",
                        "displacement_cc": 1971,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 72,
                        "power_rpm": "5200",
                        "torque_nm": 160,
                        "torque_rpm": "3000",
                        "compression_ratio": "8.8:1",
                        "valvetrain": "OHV 8-valve, wet cylinder liners",
                        "notes": "Slant-mounted all-alloy head engine."
                    },
                    {
                        "engine_code": "KF6",
                        "name": "2.0L Mechanical Injection (TI)",
                        "displacement_cc": 1971,
                        "displacement_litres": 2.0,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 78,
                        "power_rpm": "5600",
                        "torque_nm": 169,
                        "torque_rpm": "3000",
                        "compression_ratio": "8.8:1",
                        "valvetrain": "OHV 8-valve, Kugelfischer injection",
                        "notes": "Fitted to the sports 504 TI sedan."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "504 GL",
                        "years": {"start": 1969, "end": 1983},
                        "body_styles": ["4-door sedan", "5-door wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual", "3-speed ZF automatic"],
                        "msrp_aud_min": 3890,
                        "msrp_aud_max": 9950,
                        "fuel_consumption_l_100km": 10.2,
                        "kerb_weight_kg": 1210,
                        "standard_features": ["Independent rear suspension", "Four-wheel disc brakes", "Fully reclining front seats", "Plush velour upholstery"],
                        "notes": "Locally assembled Australian market backbone."
                    },
                    {
                        "badge_name": "504 TI",
                        "years": {"start": 1974, "end": 1980},
                        "body_styles": ["4-door sedan"],
                        "drivetrain": "RWD",
                        "transmissions": ["4-speed manual"],
                        "msrp_aud_min": 6490,
                        "msrp_aud_max": 9450,
                        "fuel_consumption_l_100km": 9.8,
                        "kerb_weight_kg": 1225,
                        "standard_features": ["Kugelfischer mechanical fuel injection", "Tachometer", "Dunlop SP tyres", "Front head restraints"],
                        "notes": "High-performance touring sedan."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "504 GL",
                        "body_style": "4-door sedan",
                        "engine_code": "XN1",
                        "transmission": "4-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1972,
                        "years_end": "1980",
                        "msrp_aud": 4995,
                        "power_kw": 72,
                        "torque_nm": 160,
                        "fuel_l_100km": 10.2,
                        "towing_braked_kg": 1200,
                        "notes": "Heidelberg assembled specification."
                    }
                ],
                "manuals": [],
                "pictures": []
            },
            {
                "series_code": "505",
                "generation_name": "Peugeot 505",
                "years": {"start": 1980, "end": "1993"},
                "body_styles": ["4-door sedan", "5-door wagon"],
                "platform": "Peugeot 505",
                "ancap_rating": "Unrated (Pre-ANCAP)",
                "summary": "The last rear-wheel drive Peugeot, assembled in Victoria until 1986. Pininfarina styling, 2.2L Douvrin all-alloy engine, power steering, and cavernous 8-seat Familiale.",
                "engines": [
                    {
                        "engine_code": "ZDJK (Douvrin)",
                        "name": "2.2L OHC Petrol (STI/GTI)",
                        "displacement_cc": 2165,
                        "displacement_litres": 2.2,
                        "cylinders": 4,
                        "configuration": "Inline-4",
                        "aspiration": "Naturally Aspirated",
                        "fuel_type": "Petrol",
                        "power_kw": 85,
                        "power_rpm": "5250",
                        "torque_nm": 178,
                        "torque_rpm": "3500",
                        "compression_ratio": "9.8:1",
                        "valvetrain": "SOHC 8-valve, Bosch L-Jetronic",
                        "notes": "All-alloy engine co-developed with Renault."
                    }
                ],
                "badges": [
                    {
                        "badge_name": "505 GTI",
                        "years": {"start": 1984, "end": 1993},
                        "body_styles": ["4-door sedan", "5-door wagon"],
                        "drivetrain": "RWD",
                        "transmissions": ["5-speed manual", "4-speed ZF automatic"],
                        "msrp_aud_min": 24900,
                        "msrp_aud_max": 38900,
                        "fuel_consumption_l_100km": 9.5,
                        "kerb_weight_kg": 1280,
                        "standard_features": ["Alloy wheels", "Power windows", "Central locking", "Air conditioning", "Velour interior", "Rear disc brakes"],
                        "notes": "Supreme long-distance touring comfort on rural Australian roads."
                    }
                ],
                "configurations": [
                    {
                        "badge_name": "505 GTI",
                        "body_style": "4-door sedan",
                        "engine_code": "ZDJK (Douvrin)",
                        "transmission": "5-speed manual",
                        "drivetrain": "RWD",
                        "years_start": 1985,
                        "years_end": "1991",
                        "msrp_aud": 28990,
                        "power_kw": 85,
                        "torque_nm": 178,
                        "fuel_l_100km": 9.5,
                        "towing_braked_kg": 1300,
                        "notes": "Classic rear-wheel-drive French executive sedan."
                    }
                ],
                "manuals": [],
                "pictures": []
            }
        ]
    }
}
