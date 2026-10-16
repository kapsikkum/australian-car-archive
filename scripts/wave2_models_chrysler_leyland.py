"""
Wave 2 Deep-Dive Model Data: Chrysler/Valiant and Leyland Australia Icons
Models:
21. Chrysler Centura
22. Chrysler / Mitsubishi Sigma
23. Dodge Phoenix
24. Austin 1800
25. Morris Major / Austin Freeway & Wolseley 24/80
"""
from typing import Any, Dict

MODEL_CENTURA: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "model_slug": "centura",
    "name": "Chrysler Centura",
    "vehicle_type": "4-door Sedan",
    "segment": "Mid-size",
    "years_sold_au": {"start": 1975, "end": 1978},
    "locally_built": True,
    "assembly_plants_au": [
        "Tonsley Park, Adelaide, South Australia"
    ],
    "overview": "The Chrysler Centura (KB and KC series) was Chrysler Australia's audacious weapon to conquer the mid-size family car market dominated by the Holden Torana and Ford Cortina. Assembled at Tonsley Park in Adelaide, Chrysler imported European Simca 180 bodyshells from France and undertook radical local re-engineering to shoehorn Chrysler Australia's mighty Australian-cast 3.5L (Hemi 215) and 4.0L (Hemi 245) pushrod straight-six engines, alongside a French 2.0L Simca 4-cylinder. With 123 kW (165 hp) and 319 Nm of torque propelling a compact 1,200 kg body, the Hemi 245 Centura was an astonishing sleeper muscle sedan, sprinting from 0-100 km/h in under 9 seconds and completing the standing quarter-mile in 16.5 seconds. 19,770 units were produced across the KB (1975-1977) and updated KC (1977-1978).",
    "australian_market_notes": "The Centura's Australian introduction was famously sabotaged by history: in 1973, French union wharf bans in protest of French atmospheric nuclear testing in the South Pacific delayed imported Simca bodyshell shipments for over twelve months. Unassembled bodyshells weathered on Adelaide wharves before assembly commenced in 1975. Despite this, Australian performance drivers loved the car's sensational straight-line speed, and it enjoyed a formidable track career in production car rallying and circuit racing.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "KB",
            "generation_name": "KB Centura",
            "years": {"start": 1975, "end": 1977},
            "body_styles": ["4-door sedan"],
            "platform": "Chrysler-Simca 180 unibody (modified front structure)",
            "ancap_rating": None,
            "summary": "First Centura series. Modified front sheetmetal, heavy-duty front crossmember, MacPherson strut suspension, and Australian Hemi 215 and 245 straight-six engines.",
            "engines": [
                {
                    "engine_code": "Simca-Type-315-2.0L",
                    "name": "Simca Type 315 2.0L OHC Inline-4",
                    "displacement_cc": 1981,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 71.0,
                    "power_rpm": "5600",
                    "torque_nm": 152.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.4:1",
                    "valvetrain": "SOHC 8V",
                    "notes": "French-sourced OHC four-cylinder with twin-choke Solex carburettor."
                },
                {
                    "engine_code": "Hemi-215-I6",
                    "name": "Chrysler Hemi 215 (3.5L) OHV Inline-6",
                    "displacement_cc": 3523,
                    "displacement_litres": 3.5,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "4400",
                    "torque_nm": 283.0,
                    "torque_rpm": "1800",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V Hemi",
                    "notes": "Australian-cast Hemi-head straight-six with Carter 1-barrel carburettor."
                },
                {
                    "engine_code": "Hemi-245-I6",
                    "name": "Chrysler Hemi 245 (4.0L) OHV Inline-6",
                    "displacement_cc": 4014,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 123.0,
                    "power_rpm": "4400",
                    "torque_nm": 319.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 12V Hemi",
                    "notes": "Carter twin-barrel BBD carburettor; 165 bhp output in a 1,200 kg body."
                }
            ],
            "badges": [
                {
                    "badge_name": "Centura GL 245",
                    "years": {"start": 1975, "end": 1977},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "4-speed manual floor Borg-Warner", "3-speed automatic Borg-Warner 35"],
                    "msrp_aud_min": 4390,
                    "msrp_aud_max": 4980,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1215,
                    "standard_features": [
                        "4.0L Hemi 245 straight-six standard",
                        "Front power disc brakes",
                        "Reclining front bucket seats",
                        "Collapsible steering column and flow-through ventilation"
                    ],
                    "notes": "High-volume performance family sedan."
                },
                {
                    "badge_name": "Centura GLX 245",
                    "years": {"start": 1975, "end": 1977},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor Borg-Warner", "3-speed automatic Borg-Warner 35"],
                    "msrp_aud_min": 4890,
                    "msrp_aud_max": 5450,
                    "fuel_consumption_l_100km": 12.8,
                    "kerb_weight_kg": 1230,
                    "standard_features": [
                        "Sports dashboard with tachometer and oil pressure gauges",
                        "Vinyl roof and dual body side pin-striping",
                        "Sports steering wheel and center console",
                        "Carpeting throughout and rear center armrest",
                        "Sports road wheels"
                    ],
                    "notes": "Sports luxury flagship model."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Centura GLX 245",
                    "body_style": "Sedan",
                    "engine_code": "Hemi-245-I6",
                    "transmission": "4-speed manual floor Borg-Warner",
                    "drivetrain": "RWD",
                    "msrp_aud": 4890,
                    "power_kw": 123.0,
                    "torque_nm": 319.0,
                    "fuel_l_100km": 12.8,
                    "towing_braked_kg": 1200,
                    "notes": "123 kW 4.0L Hemi 4-speed manual sleeper sedan."
                }
            ]
        },
        {
            "series_code": "KC",
            "generation_name": "KC Centura",
            "years": {"start": 1977, "end": 1978},
            "body_styles": ["4-door sedan"],
            "platform": "Chrysler-Simca 180 unibody",
            "ancap_rating": None,
            "summary": "Facelifted front grille with Chrysler pentastar, improved sound insulation, revised suspension geometry, and ADR27A anti-pollution updates.",
            "engines": [
                {
                    "engine_code": "Hemi-245-I6-ADR27A",
                    "name": "Chrysler Hemi 245 (4.0L) ADR27A Inline-6",
                    "displacement_cc": 4014,
                    "displacement_litres": 4.0,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 104.0,
                    "power_rpm": "4000",
                    "torque_nm": 305.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 12V Hemi",
                    "notes": "Revised for ADR27A emission regulations."
                }
            ],
            "badges": [
                {
                    "badge_name": "Centura GL 245",
                    "years": {"start": 1977, "end": 1978},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor", "3-speed automatic"],
                    "msrp_aud_min": 5190,
                    "msrp_aud_max": 5790,
                    "fuel_consumption_l_100km": 12.5,
                    "kerb_weight_kg": 1225,
                    "standard_features": [
                        "Restyled grille and body side mouldings",
                        "Radial-ply tyres and front sway bar",
                        "Cloth/vinyl upholstery",
                        "Push-button radio"
                    ],
                    "notes": "Refined second series."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Centura GL 245",
                    "body_style": "Sedan",
                    "engine_code": "Hemi-245-I6-ADR27A",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 5190,
                    "power_kw": 104.0,
                    "torque_nm": 305.0,
                    "fuel_l_100km": 12.5,
                    "towing_braked_kg": 1200,
                    "notes": "4.0L Hemi family sedan."
                }
            ]
        }
    ]
}

MODEL_SIGMA: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "model_slug": "sigma",
    "name": "Chrysler / Mitsubishi Sigma",
    "vehicle_type": "4-door Sedan / 5-door Station Wagon",
    "segment": "Mid-size",
    "years_sold_au": {"start": 1977, "end": 1987},
    "locally_built": True,
    "assembly_plants_au": [
        "Tonsley Park, Adelaide, South Australia"
    ],
    "overview": "The Chrysler Sigma—later renamed Mitsubishi Sigma after Mitsubishi acquired Chrysler Australia in 1980—was the undisputed king of Australia's four-cylinder family car market across the late 1970s and 1980s. Manufactured at Tonsley Park in Adelaide, the Sigma (GE, GH, GJ, GK, GN) dethroned traditional six-cylinder cars by offering expansive interior space, European-influenced styling, four-wheel coil spring suspension, and revolutionary 'Silent Shaft' counter-rotating balance shafts in its Australian-cast Astron 1.85L, 2.0L, and 2.6L engines. The GH series introduced the legendary limited-edition Sigma Turbo in 1981 (Australia's first locally built turbocharged production car), while the 1982 GJ series spawned the celebrated Peter Wherrett Special. Over 300,000 Sigmas were built in Adelaide before making way for the Magna.",
    "australian_market_notes": "The Sigma completely altered Australian buying habits, proving that a smooth, balance-shaft four-cylinder car could equal or exceed a traditional Australian straight-six in refinement and towing capability. The Australian-built Sigma Wagon featured a unique Australian-engineered cargo floor and rear roofline not found on Japanese Galants, providing superior cargo volume.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "GE-GH",
            "generation_name": "GE / GH Chrysler Sigma & Sigma Turbo",
            "years": {"start": 1977, "end": 1982},
            "body_styles": ["4-door sedan", "5-door wagon"],
            "platform": "Mitsubishi Galant / Chrysler Australia unibody",
            "ancap_rating": None,
            "summary": "First Australian Sigma series. Astron Silent Shaft engine with balance shafts, 4-wheel coil suspension, four-wheel disc brakes on SE, and the historic 1981 GH Sigma Turbo.",
            "engines": [
                {
                    "engine_code": "Astron-2.0L-SilentShaft",
                    "name": "Chrysler / Mitsubishi Astron 2.0L OHC Inline-4",
                    "displacement_cc": 1995,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 70.0,
                    "power_rpm": "5400",
                    "torque_nm": 152.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8V Silent Shaft",
                    "notes": "Patented twin counter-rotating balance shafts for six-cylinder smoothness."
                },
                {
                    "engine_code": "Astron-2.6L-SilentShaft",
                    "name": "Chrysler / Mitsubishi Astron 2.6L OHC Inline-4",
                    "displacement_cc": 2555,
                    "displacement_litres": 2.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 76.0,
                    "power_rpm": "4800",
                    "torque_nm": 192.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "SOHC 8V Silent Shaft",
                    "notes": "World's largest four-cylinder passenger car engine at the time; manufactured at Lonsdale, SA."
                },
                {
                    "engine_code": "Astron-2.0L-Turbo-GH",
                    "name": "Mitsubishi Astron 2.0L Turbocharged OHC Inline-4",
                    "displacement_cc": 1995,
                    "displacement_litres": 2.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Petrol",
                    "power_kw": 116.0,
                    "power_rpm": "5400",
                    "torque_nm": 235.0,
                    "torque_rpm": "3200",
                    "compression_ratio": "7.6:1",
                    "valvetrain": "SOHC 8V Silent Shaft",
                    "notes": "Garrett AiResearch T03 turbocharger, sodium-filled exhaust valves; Australia's first locally built turbo car."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sigma SE 2.6",
                    "years": {"start": 1980, "end": 1982},
                    "body_styles": ["Sedan", "Wagon"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual", "3-speed automatic Borg-Warner 45"],
                    "msrp_aud_min": 7890,
                    "msrp_aud_max": 8990,
                    "fuel_consumption_l_100km": 10.2,
                    "kerb_weight_kg": 1140,
                    "standard_features": [
                        "2.6L Astron Silent Shaft engine standard",
                        "Four-wheel power disc brakes",
                        "Velour upholstery and cut-pile carpeting",
                        "Overhead console with map reading lamps",
                        "Cast alloy wheels and tinted glass"
                    ],
                    "notes": "Top-tier luxury family saloon."
                },
                {
                    "badge_name": "Sigma Turbo (GH)",
                    "years": {"start": 1981, "end": 1981},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual heavy duty"],
                    "msrp_aud_min": 11990,
                    "msrp_aud_max": 12500,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1180,
                    "standard_features": [
                        "116 kW (156 hp) 2.0L Garrett Turbo engine",
                        "Four-wheel disc brakes and sports suspension",
                        "Distinctive front air dam, rear spoiler, and 'TURBO' side graphics",
                        "15-inch alloy wheels and Pirelli Cinturato P6 tyres",
                        "Sports dashboard with turbo boost pressure gauge"
                    ],
                    "notes": "Australia's first factory turbo production car; strictly 500 built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sigma SE 2.6",
                    "body_style": "Sedan",
                    "engine_code": "Astron-2.6L-SilentShaft",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "msrp_aud": 7890,
                    "power_kw": 76.0,
                    "torque_nm": 192.0,
                    "fuel_l_100km": 10.2,
                    "towing_braked_kg": 1200,
                    "notes": "2.6L Astron 5-speed luxury family sedan."
                },
                {
                    "badge_name": "Sigma Turbo (GH)",
                    "body_style": "Sedan",
                    "engine_code": "Astron-2.0L-Turbo-GH",
                    "transmission": "5-speed manual heavy duty",
                    "drivetrain": "RWD",
                    "msrp_aud": 11990,
                    "power_kw": 116.0,
                    "torque_nm": 235.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1100,
                    "notes": "Historic Australian factory turbocharged road car."
                }
            ]
        },
        {
            "series_code": "GJ-GK-GN",
            "generation_name": "GJ / GK / GN Mitsubishi Sigma",
            "years": {"start": 1982, "end": 1987},
            "body_styles": ["4-door sedan", "5-door wagon"],
            "platform": "Mitsubishi Sigma Australian unibody",
            "ancap_rating": None,
            "summary": "Crisp squared Australian restyle by Mitsubishi Motors Australia Ltd (MMAL). Introduction of the handling-tuned Peter Wherrett Special and luxurious Super Saloon.",
            "engines": [
                {
                    "engine_code": "Astron-II-2.6L",
                    "name": "Mitsubishi Astron II 2.6L OHC Inline-4",
                    "displacement_cc": 2555,
                    "displacement_litres": 2.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 76.0,
                    "power_rpm": "4800",
                    "torque_nm": 192.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "8.5:1",
                    "valvetrain": "SOHC 8V Silent Shaft",
                    "notes": "Astron II cylinder head with hydraulic lash adjusters and MCA-Jet valve."
                }
            ],
            "badges": [
                {
                    "badge_name": "Peter Wherrett Special (GJ)",
                    "years": {"start": 1982, "end": 1983},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["5-speed manual"],
                    "msrp_aud_min": 10500,
                    "msrp_aud_max": 10990,
                    "fuel_consumption_l_100km": 10.4,
                    "kerb_weight_kg": 1150,
                    "standard_features": [
                        "Suspension tuned by ABC motoring journalist Peter Wherrett",
                        "Recaro high-bolster front bucket seats",
                        "Momo leather sports steering wheel and gear knob",
                        "15-inch Globe alloy wheels and high-performance tyres",
                        "Distinctive two-tone silver paint and front/rear spoilers"
                    ],
                    "notes": "Celebrated Australian journalist-tuned sports special; 1000 built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Peter Wherrett Special (GJ)",
                    "body_style": "Sedan",
                    "engine_code": "Astron-II-2.6L",
                    "transmission": "5-speed manual",
                    "drivetrain": "RWD",
                    "msrp_aud": 10500,
                    "power_kw": 76.0,
                    "torque_nm": 192.0,
                    "fuel_l_100km": 10.4,
                    "towing_braked_kg": 1200,
                    "notes": "Peter Wherrett suspension tuned sports sedan."
                }
            ]
        }
    ]
}

MODEL_DODGE_PHOENIX: Dict[str, Any] = {
    "make_slug": "chrysler-valiant",
    "model_slug": "dodge-phoenix",
    "name": "Dodge Phoenix",
    "vehicle_type": "4-door Sedan / 4-door Hardtop (pillarless)",
    "segment": "Luxury Full-size American Flagship",
    "years_sold_au": {"start": 1960, "end": 1973},
    "locally_built": True,
    "assembly_plants_au": [
        "Mile End, Adelaide, South Australia (1960-1964)",
        "Tonsley Park, Adelaide, South Australia (1964-1973)"
    ],
    "overview": "The Dodge Phoenix was Chrysler Australia's grand American luxury flagship from 1960 to 1973. Conceived to compete head-on with the Ford Galaxie and Chevrolet Impala/Bel Air in the prestige government, executive, and pastoralist market, the Phoenix was assembled in Adelaide from North American CKD packs, using Dodge Dart/Polara, Plymouth Fury, and Chrysler bodies married to bespoke factory right-hand drive Plymouth dashboards. Spanning the early finned PD/RD series through to the majestic 'fuselage'-bodied models of 1969-1973, every Phoenix was powered by burly American Chrysler V8 engines—predominantly the 318ci (5.2L) 'Poly' and 'LA' small-block V8s, and the optional 383ci (6.3L) 'B-block' Big Block V8 in the opulent Phoenix 400 Hardtop. Sumptuously appointed with Torqueflite 3-speed automatic transmissions, power steering, push-button radios, and deep plush interiors, the Phoenix was the undisputed car of choice for Australian politicians, judges, and graziers.",
    "australian_market_notes": "Because full right-hand drive manufacturing of American full-size cars ceased in North America, Chrysler Australia created bespoke tooling at Tonsley Park to assemble the Phoenix with right-hand drive steering boxes, Australian-made glass, batteries, tyres, and interior trim. The pillarless 400 Hardtop introduced in 1967 represented the absolute summit of Chrysler Australia luxury before the model was retired in 1973.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "PD-PF",
            "generation_name": "PD / PF Dodge Phoenix",
            "years": {"start": 1960, "end": 1964},
            "body_styles": ["4-door sedan"],
            "platform": "Chrysler B-body unibody architecture",
            "ancap_rating": None,
            "summary": "Early finned tail and slab-side Plymouth Fury-derived body, assembled at Mile End, Adelaide. Powered by the 318ci 'Poly' V8 with push-button Torqueflite automatic.",
            "engines": [
                {
                    "engine_code": "Poly-318-V8",
                    "name": "Chrysler 'Poly' 318ci (5.2L) V8",
                    "displacement_cc": 5211,
                    "displacement_litres": 5.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 168.0,
                    "power_rpm": "4400",
                    "torque_nm": 420.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V Polyspherical",
                    "notes": "Polyspherical combustion chamber V8; Carter 2-barrel carburettor; 225 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "Phoenix Sedan",
                    "years": {"start": 1960, "end": 1964},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed push-button Torqueflite automatic"],
                    "msrp_aud_min": 4400,
                    "msrp_aud_max": 4850,
                    "fuel_consumption_l_100km": 16.5,
                    "kerb_weight_kg": 1640,
                    "standard_features": [
                        "318 Poly V8 engine",
                        "Push-button dashboard Torqueflite transmission control",
                        "Torsion-Aire front torsion bar suspension",
                        "Power steering and power drum brakes",
                        "Full-width bench seating for six with deep foam padding"
                    ],
                    "notes": "Luxury American flagship sedan."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Phoenix Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Poly-318-V8",
                    "transmission": "3-speed push-button Torqueflite automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 4400,
                    "power_kw": 168.0,
                    "torque_nm": 420.0,
                    "fuel_l_100km": 16.5,
                    "towing_braked_kg": 1600,
                    "notes": "Classic push-button Torqueflite 318 V8 sedan."
                }
            ]
        },
        {
            "series_code": "DB-RD",
            "generation_name": "DB / RD Dodge Phoenix & 400 Hardtop",
            "years": {"start": 1965, "end": 1973},
            "body_styles": ["4-door sedan", "4-door pillarless hardtop"],
            "platform": "Chrysler C-body unibody architecture",
            "ancap_rating": None,
            "summary": "Long-wheelbase full-size luxury cruiser and iconic 'fuselage' body styling from 1969. Assembled at Tonsley Park with 318ci LA V8 and 383ci Big Block in Phoenix 400 Hardtop.",
            "engines": [
                {
                    "engine_code": "LA-318-V8-Phoenix",
                    "name": "Chrysler LA 318ci (5.2L) OHV V8",
                    "displacement_cc": 5211,
                    "displacement_litres": 5.2,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 172.0,
                    "power_rpm": "4400",
                    "torque_nm": 461.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Lightweight wedge-head small-block V8; standard on Phoenix Sedan."
                },
                {
                    "engine_code": "BigBlock-383-V8",
                    "name": "Chrysler 'B' 383ci (6.3L) Big Block V8",
                    "displacement_cc": 6277,
                    "displacement_litres": 6.3,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 201.0,
                    "power_rpm": "4400",
                    "torque_nm": 529.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.2:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Carter 2-barrel carburettor; 270 bhp and 390 lb-ft torque; exclusive to Phoenix 400 Hardtop."
                }
            ],
            "badges": [
                {
                    "badge_name": "Phoenix 400 Hardtop",
                    "years": {"start": 1967, "end": 1973},
                    "body_styles": ["Hardtop"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed column Torqueflite automatic"],
                    "msrp_aud_min": 5990,
                    "msrp_aud_max": 7250,
                    "fuel_consumption_l_100km": 18.5,
                    "kerb_weight_kg": 1860,
                    "standard_features": [
                        "383ci 6.3L Big Block V8 standard",
                        "Pillarless 4-door hardtop roofline",
                        "Glove-soft pleated vinyl upholstery and deep cut-pile carpets",
                        "Electric power windows and power antenna",
                        "Front power disc brakes and heavy-duty front torsion bars"
                    ],
                    "notes": "Prestige flagship luxury hardtop."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Phoenix 400 Hardtop",
                    "body_style": "Hardtop",
                    "engine_code": "BigBlock-383-V8",
                    "transmission": "3-speed column Torqueflite automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 6490,
                    "power_kw": 201.0,
                    "torque_nm": 529.0,
                    "fuel_l_100km": 18.5,
                    "towing_braked_kg": 1800,
                    "notes": "383ci Big Block V8 pillarless luxury hardtop."
                }
            ]
        }
    ]
}

MODEL_AUSTIN_1800: Dict[str, Any] = {
    "make_slug": "leyland-australia",
    "model_slug": "austin-1800",
    "name": "Austin 1800 / Utility (Landcrab)",
    "vehicle_type": "4-door Sedan / 2-door Coupe Utility",
    "segment": "Mid-size / Large",
    "years_sold_au": {"start": 1965, "end": 1971},
    "locally_built": True,
    "assembly_plants_au": [
        "Victoria Park (Zetland), Sydney, New South Wales"
    ],
    "overview": "The Austin 1800 (BMC project ADO17, affectionately nicknamed the 'Landcrab' for its broad track and tenacious roadholding) was manufactured in Australia by BMC and later Leyland Australia at the Victoria Park assembly complex in Zetland, Sydney. Featuring Alec Issigonis's revolutionary transverse engine front-wheel-drive layout, Hydrolastic interconnected fluid suspension, and an astonishingly spacious passenger cabin with 70% of car length devoted to passengers, the 1800 won Wheels Car of the Year in 1965. Australia made two world-exclusive contributions to the model: Australian engineers re-engineered the shell with elevated ground clearance and sump protection for outback endurance (proven by an astonishing 2nd place in the gruelling 1968 London-to-Sydney Marathon); and in 1968, Leyland Australia designed and manufactured the world's only Austin 1800 Utility ('Landcrab Ute'), combining front-wheel drive, a completely flat load bed, and Hydrolastic self-levelling suspension that kept the ute flat regardless of cargo weight! Over 56,000 Austin 1800s were built in Sydney.",
    "australian_market_notes": "The Australian-developed Austin 1800 Utility was an engineering triumph. Because front-wheel drive eliminated the transmission tunnel and rear differential, the load bed was totally flat with incredible capacity. Combined with the Hydrolastic interconnected suspension, the rear never sagged under load. The 1800 'S' saloon added twin SU carburettors, a sports cam, and 72 kW (96 bhp) performance.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Mk-I",
            "generation_name": "Mk I Austin 1800",
            "years": {"start": 1965, "end": 1968},
            "body_styles": ["4-door sedan"],
            "platform": "BMC ADO17 unibody",
            "ancap_rating": None,
            "summary": "Wheels Car of the Year 1965. Transverse 1.8L BMC B-series engine, Hydrolastic fluid suspension, front-wheel drive, and massive interior legroom.",
            "engines": [
                {
                    "engine_code": "BMC-B-Series-1.8L",
                    "name": "BMC B-Series 1.8L OHV Inline-4",
                    "displacement_cc": 1798,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 63.0,
                    "power_rpm": "5300",
                    "torque_nm": 134.0,
                    "torque_rpm": "2100",
                    "compression_ratio": "8.4:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Single SU HS6 carburettor, 5-bearing crankshaft, transverse gearbox-in-sump."
                }
            ],
            "badges": [
                {
                    "badge_name": "1800 Saloon",
                    "years": {"start": 1965, "end": 1968},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 2340,
                    "msrp_aud_max": 2550,
                    "fuel_consumption_l_100km": 9.2,
                    "kerb_weight_kg": 1170,
                    "standard_features": [
                        "Hydrolastic interconnected fluid suspension",
                        "Front disc brakes",
                        "Transverse front-wheel drive packaging",
                        "Huge rear legroom exceeding traditional large cars"
                    ],
                    "notes": "Wheels Car of the Year winner."
                }
            ],
            "configurations": [
                {
                    "badge_name": "1800 Saloon",
                    "body_style": "Sedan",
                    "engine_code": "BMC-B-Series-1.8L",
                    "transmission": "4-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 2340,
                    "power_kw": 63.0,
                    "torque_nm": 134.0,
                    "fuel_l_100km": 9.2,
                    "towing_braked_kg": 900,
                    "notes": "Transverse FWD Australian family car."
                }
            ]
        },
        {
            "series_code": "Mk-II",
            "generation_name": "Mk II Austin 1800 & Utility",
            "years": {"start": 1968, "end": 1971},
            "body_styles": ["4-door sedan", "2-door coupe utility"],
            "platform": "BMC ADO17 unibody",
            "ancap_rating": None,
            "summary": "Introduction of the world-exclusive Australian-designed Austin 1800 Utility, upright rear tail fins, twin-carburettor 1800 'S' saloon, and optional Borg-Warner 35 automatic.",
            "engines": [
                {
                    "engine_code": "BMC-B-Series-1.8L-MkII",
                    "name": "BMC B-Series 1.8L Mk II Inline-4",
                    "displacement_cc": 1798,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 65.0,
                    "power_rpm": "5300",
                    "torque_nm": 137.0,
                    "torque_rpm": "2100",
                    "compression_ratio": "8.6:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Single SU carburettor with revised cylinder head ports."
                },
                {
                    "engine_code": "BMC-B-Series-1.8S-TwinSU",
                    "name": "BMC B-Series 1.8L 'S' Twin-SU Inline-4",
                    "displacement_cc": 1798,
                    "displacement_litres": 1.8,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 72.0,
                    "power_rpm": "5600",
                    "torque_nm": 144.0,
                    "torque_rpm": "3000",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Twin SU HS6 carburettors, free-flow exhaust manifold; 96 bhp; powers 1800 'S'."
                }
            ],
            "badges": [
                {
                    "badge_name": "Austin 1800 Utility",
                    "years": {"start": 1968, "end": 1971},
                    "body_styles": ["Coupe Utility"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 2190,
                    "msrp_aud_max": 2390,
                    "fuel_consumption_l_100km": 9.5,
                    "kerb_weight_kg": 1130,
                    "standard_features": [
                        "Australian-designed unibody coupe utility",
                        "Hydrolastic fluid suspension maintaining level bed height under load",
                        "Flat uninterrupted cargo bed with no driveshaft hump",
                        "Half-tonne payload rating",
                        "Full-width bench seating with durable commercial vinyl"
                    ],
                    "notes": "World-exclusive Australian-developed FWD commercial ute."
                },
                {
                    "badge_name": "Austin 1800 'S' Saloon",
                    "years": {"start": 1968, "end": 1971},
                    "body_styles": ["Sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed manual"],
                    "msrp_aud_min": 2690,
                    "msrp_aud_max": 2890,
                    "fuel_consumption_l_100km": 9.6,
                    "kerb_weight_kg": 1180,
                    "standard_features": [
                        "Twin SU 72 kW 'S' performance engine",
                        "Sports instrumentation with tachometer",
                        "Upright tailfins with amber turn indicators",
                        "Power front disc brakes",
                        "Reclining front bucket seats"
                    ],
                    "notes": "High-performance sports saloon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Austin 1800 Utility",
                    "body_style": "Coupe Utility",
                    "engine_code": "BMC-B-Series-1.8L-MkII",
                    "transmission": "4-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 2190,
                    "power_kw": 65.0,
                    "torque_nm": 137.0,
                    "fuel_l_100km": 9.5,
                    "towing_braked_kg": 900,
                    "notes": "Unique Australian-designed Landcrab ute."
                },
                {
                    "badge_name": "Austin 1800 'S' Saloon",
                    "body_style": "Sedan",
                    "engine_code": "BMC-B-Series-1.8S-TwinSU",
                    "transmission": "4-speed manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 2690,
                    "power_kw": 72.0,
                    "torque_nm": 144.0,
                    "fuel_l_100km": 9.6,
                    "towing_braked_kg": 950,
                    "notes": "Twin-carburettor 72 kW sports saloon."
                }
            ]
        }
    ]
}

MODEL_MORRIS_MAJOR_FREEWAY: Dict[str, Any] = {
    "make_slug": "leyland-australia",
    "model_slug": "morris-major-freeway",
    "name": "Morris Major / Austin Freeway & Wolseley 24/80",
    "vehicle_type": "4-door Sedan / 5-door Station Wagon",
    "segment": "Compact / Mid-size",
    "years_sold_au": {"start": 1958, "end": 1965},
    "locally_built": True,
    "assembly_plants_au": [
        "Victoria Park (Zetland), Sydney, New South Wales"
    ],
    "overview": "The Morris Major and Austin Freeway family was BMC Australia's dedicated endeavor to engineer vehicles specifically for Australian motoring conditions at the Victoria Park plant in Zetland, Sydney. Commencing in 1958 as the Morris Major (and sibling Austin Lancer), it adapted the Wolseley 1500 body with increased ground clearance, reinforced suspension, and BMC's 1.5L B-Series four. In 1962, BMC Australia achieved an extraordinary domestic engineering feat: by extending the nose structure and casting two extra cylinders onto the 1622cc B-Series block, they created Australia's first locally designed mass-market inline-six: the 2433cc 'Blue Streak' six. Fitted to the Austin Freeway and the luxury Wolseley 24/80 (featuring genuine burr walnut dashboard and leather seats), the 6-cylinder Freeway competed directly with the Holden and Falcon, offering 59 kW, outback suspension, and optional Borg-Warner 35 automatic transmission.",
    "australian_market_notes": "The 2.4-litre 'Blue Streak' engine was cast and machined entirely in Australia at BMC's Zetland engine facility. It used common pistons, conrods, and valvegear with the 4-cylinder B-series, achieving brilliant manufacturing economies. The Austin Freeway Station Wagon offered immense load space and was standard equipment for many Australian municipal councils and outback traveling salesmen.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Major-Series-I-II-Elite",
            "generation_name": "Morris Major (Series I, II & Elite)",
            "years": {"start": 1958, "end": 1964},
            "body_styles": ["4-door sedan"],
            "platform": "BMC Australian unibody (Wolseley 1500 derivative)",
            "ancap_rating": None,
            "summary": "Australian-developed 4-cylinder compact sedan. Higher ride clearance, heavy-duty suspension, 1.5L B-Series engine, followed by 1.6L Elite with finned rear wings.",
            "engines": [
                {
                    "engine_code": "BMC-B-Series-1500",
                    "name": "BMC B-Series 1.5L OHV Inline-4",
                    "displacement_cc": 1489,
                    "displacement_litres": 1.5,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 37.0,
                    "power_rpm": "4200",
                    "torque_nm": 102.0,
                    "torque_rpm": "2400",
                    "compression_ratio": "7.2:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Single SU carburettor, 50 bhp output."
                },
                {
                    "engine_code": "BMC-B-Series-1622",
                    "name": "BMC B-Series 1.6L OHV Inline-4",
                    "displacement_cc": 1622,
                    "displacement_litres": 1.6,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 45.0,
                    "power_rpm": "4500",
                    "torque_nm": 122.0,
                    "torque_rpm": "2500",
                    "compression_ratio": "8.3:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Fitted to Morris Major Elite; 60 bhp output."
                }
            ],
            "badges": [
                {
                    "badge_name": "Morris Major Elite",
                    "years": {"start": 1962, "end": 1964},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual floor"],
                    "msrp_aud_min": 1780,
                    "msrp_aud_max": 1890,
                    "fuel_consumption_l_100km": 8.5,
                    "kerb_weight_kg": 950,
                    "standard_features": [
                        "1622cc B-Series engine with 60 bhp",
                        "New tail fin styling with wrap-around tail lights",
                        "Heavy-duty front torsion bar and rear leaf spring suspension",
                        "Vinyl bench seats and fresh-air heater/demister"
                    ],
                    "notes": "Final and most refined Morris Major."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Morris Major Elite",
                    "body_style": "Sedan",
                    "engine_code": "BMC-B-Series-1622",
                    "transmission": "4-speed manual floor",
                    "drivetrain": "RWD",
                    "msrp_aud": 1780,
                    "power_kw": 45.0,
                    "torque_nm": 122.0,
                    "fuel_l_100km": 8.5,
                    "towing_braked_kg": 750,
                    "notes": "1.6L Australian-developed compact."
                }
            ]
        },
        {
            "series_code": "Freeway-Wolseley-24-80",
            "generation_name": "Austin Freeway & Wolseley 24/80 (6-Cylinder)",
            "years": {"start": 1962, "end": 1965},
            "body_styles": ["4-door sedan", "5-door wagon"],
            "platform": "BMC Australian lengthened unibody",
            "ancap_rating": None,
            "summary": "First Australian-designed mass-production inline-six: the 2.4L 'Blue Streak' six. Austin Freeway sedan and wagon, and prestige Wolseley 24/80 with burr walnut dash.",
            "engines": [
                {
                    "engine_code": "Blue-Streak-2433-I6",
                    "name": "BMC Blue Streak 2.4L OHV Inline-6",
                    "displacement_cc": 2433,
                    "displacement_litres": 2.4,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 59.0,
                    "power_rpm": "4350",
                    "torque_nm": 167.0,
                    "torque_rpm": "1750",
                    "compression_ratio": "8.2:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Single SU HS4 carburettor; 80 bhp and 123 lb-ft torque at low rpm."
                },
                {
                    "engine_code": "Blue-Streak-2433-TwinSU",
                    "name": "BMC Blue Streak 2.4L Twin-SU Inline-6",
                    "displacement_cc": 2433,
                    "displacement_litres": 2.4,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 63.0,
                    "power_rpm": "4400",
                    "torque_nm": 174.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "8.3:1",
                    "valvetrain": "OHV 12V",
                    "notes": "Twin SU HS4 carburettors; 85 bhp; exclusive to Wolseley 24/80 Mk II."
                }
            ],
            "badges": [
                {
                    "badge_name": "Austin Freeway Sedan",
                    "years": {"start": 1962, "end": 1965},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column with synchromesh on all gears", "Borg-Warner 35 3-speed automatic"],
                    "msrp_aud_min": 2180,
                    "msrp_aud_max": 2390,
                    "fuel_consumption_l_100km": 10.8,
                    "kerb_weight_kg": 1150,
                    "standard_features": [
                        "2.4L Blue Streak 6-cylinder engine",
                        "3-speed all-synchromesh manual transmission",
                        "Heavy-duty outback radiator and suspension",
                        "Wide chrome horizontal front grille with integrated indicators",
                        "Full-width bench seating for six"
                    ],
                    "notes": "Competitor to Holden Special and Ford Falcon."
                },
                {
                    "badge_name": "Wolseley 24/80 Sedan",
                    "years": {"start": 1962, "end": 1965},
                    "body_styles": ["Sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed manual column", "Borg-Warner 35 3-speed automatic"],
                    "msrp_aud_min": 2450,
                    "msrp_aud_max": 2690,
                    "fuel_consumption_l_100km": 11.2,
                    "kerb_weight_kg": 1190,
                    "standard_features": [
                        "2.4L Blue Streak 6-cylinder engine (twin SU carbs on Mk II)",
                        "Illuminated Wolseley radiator badge emblem",
                        "Genuine burr walnut timber veneer dashboard and door cappings",
                        "Deep English leather upholstery",
                        "Deep pile carpets and sound insulation package"
                    ],
                    "notes": "Luxury 6-cylinder executive saloon."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Austin Freeway Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Blue-Streak-2433-I6",
                    "transmission": "3-speed manual column with synchromesh on all gears",
                    "drivetrain": "RWD",
                    "msrp_aud": 2180,
                    "power_kw": 59.0,
                    "torque_nm": 167.0,
                    "fuel_l_100km": 10.8,
                    "towing_braked_kg": 950,
                    "notes": "2.4L Blue Streak 6-cylinder family sedan."
                },
                {
                    "badge_name": "Wolseley 24/80 Sedan",
                    "body_style": "Sedan",
                    "engine_code": "Blue-Streak-2433-TwinSU",
                    "transmission": "Borg-Warner 35 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 2650,
                    "power_kw": 63.0,
                    "torque_nm": 174.0,
                    "fuel_l_100km": 11.2,
                    "towing_braked_kg": 1000,
                    "notes": "Luxury walnut and leather 6-cylinder saloon."
                }
            ]
        }
    ]
}
