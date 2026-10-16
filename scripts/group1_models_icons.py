"""
Deep-dive model data for Leyland P76, Lightburn Zeta, Bolwell Nagari,
Goggomobil Dart, Giocattolo Group B, OKA 4x4, Brabham BT62, and HDT VK Group A.
"""
from typing import Any, Dict

LEYLAND_P76_DATA: Dict[str, Any] = {
    "make_slug": "leyland-australia",
    "model_slug": "leyland-p76",
    "name": "Leyland P76",
    "vehicle_type": "Sedan",
    "segment": "Full-size",
    "years_sold_au": {"start": 1973, "end": 1975},
    "locally_built": True,
    "assembly_plants_au": [
        "Zetland, New South Wales"
    ],
    "overview": "The Leyland P76 was Australia's most daring automotive gamble. Developed under project leader Peter North at BMC/Leyland's Zetland plant in Sydney to break the Holden-Ford-Chrysler monopoly, the P76 was styled by Italian master Giovanni Michelotti. It boasted world-class engineering: an all-aluminium 4.4-litre V8 derived from Rover weighing less than rivals' iron sixes, standard front power disc brakes, MacPherson strut front suspension, side-impact door bars, and a boot famously demonstrated by swallowing an entire 44-gallon drum. The P76 won the 1973 Wheels Car of the Year and conquered the 1974 World Cup Rally across the Sahara before factory closure cut short its life.",
    "australian_market_notes": "Launched in June 1973, the P76 suffered from supplier strikes and early teething quality defects that tarnished its market launch. Despite these setbacks, the car was praised by motoring journalists for exceptional ride comfort, steering precision, and fuel economy from the lightweight alloy V8. Around 18,000 sedans were built at Zetland before Leyland Australia's parent company collapsed in the UK, leading to the closure of the Sydney plant in late 1974.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "P76",
            "generation_name": "Leyland P76 Series",
            "years": {"start": 1973, "end": 1975},
            "body_styles": ["4-door full-size sedan"],
            "platform": "Leyland Australia unibody",
            "ancap_rating": None,
            "summary": "1973 Wheels Car of the Year winner; Michelotti styling, 4.4L all-alloy V8 and 2.6L OHC six; cavernous boot; Deluxe, Super, and Executive trims.",
            "engines": [
                {
                    "engine_code": "E6-2.6-OHC",
                    "name": "Leyland E-Series 2.6L OHC Inline-6",
                    "displacement_cc": 2622,
                    "displacement_litres": 2.6,
                    "cylinders": 6,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 82.0,
                    "power_rpm": "4500",
                    "torque_nm": 204.0,
                    "torque_rpm": "2000",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHC 12V",
                    "notes": "Single twin-choke downdraft carburettor."
                },
                {
                    "engine_code": "Alloy-4.4-V8",
                    "name": "Leyland 4.4L All-Aluminium V8",
                    "displacement_cc": 4416,
                    "displacement_litres": 4.4,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol",
                    "power_kw": 143.0,
                    "power_rpm": "4250",
                    "torque_nm": 386.0,
                    "torque_rpm": "2500",
                    "compression_ratio": "9.0:1",
                    "valvetrain": "OHV 16V All-Alloy Block & Heads",
                    "notes": "Stromberg twin carburettors; weighs only 220kg; exceptional power-to-weight ratio."
                }
            ],
            "badges": [
                {
                    "badge_name": "Deluxe",
                    "years": {"start": 1973, "end": 1975},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["3-speed column manual", "4-speed floor manual", "Borg-Warner 35 3-speed auto"],
                    "msrp_aud_min": 2842,
                    "msrp_aud_max": 3450,
                    "fuel_consumption_l_100km": 12.0,
                    "kerb_weight_kg": 1245,
                    "standard_features": ["Front disc brakes", "MacPherson strut suspension", "Bench front seat", "Cavernous 44-gallon drum boot"],
                    "notes": "Base specification."
                },
                {
                    "badge_name": "Executive",
                    "years": {"start": 1973, "end": 1975},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["Borg-Warner 35 3-speed automatic"],
                    "msrp_aud_min": 4104,
                    "msrp_aud_max": 4650,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1330,
                    "standard_features": ["4.4L All-Aluminium V8 standard", "Reclining bucket seats", "Power steering", "Brocade or vinyl upholstery", "Woodgrain dash fascia"],
                    "notes": "Luxury executive cruiser."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Executive",
                    "body_style": "4-door sedan",
                    "engine_code": "Alloy-4.4-V8",
                    "transmission": "Borg-Warner 35 3-speed automatic",
                    "drivetrain": "RWD",
                    "msrp_aud": 4104,
                    "power_kw": 143.0,
                    "torque_nm": 386.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 1500,
                    "notes": "1973 Wheels Car of the Year winner."
                }
            ]
        }
    ]
}

LIGHTBURN_ZETA_DATA: Dict[str, Any] = {
    "make_slug": "lightburn",
    "model_slug": "zeta-sedan",
    "name": "Lightburn Zeta Sedan",
    "vehicle_type": "Microcar",
    "segment": "Micro / City Car",
    "years_sold_au": {"start": 1963, "end": 1965},
    "locally_built": True,
    "assembly_plants_au": [
        "Camden Park, South Australia"
    ],
    "overview": "The Lightburn Zeta was South Australia's unique fiberglass microcar, manufactured by industrial equipment firm Lightburn & Co. in Camden Park, Adelaide. Powered by a British Villiers 324cc two-stroke twin-cylinder motorcycle engine driving the front wheels through a 4-speed sequential dog transaxle without reverse (the engine was stopped and restarted in reverse rotation), the Zeta was impervious to corrosion and designed to provide economical suburban motoring.",
    "australian_market_notes": "Conceived by Harold Lightburn to compete with second-hand family sedans and the BMC Mini, the Zeta featured a one-piece reinforced fiberglass body. Remarkably, it had no external boot lid—cargo was loaded over the back seat. Around 363 sedans and utilities and 28 Zeta Sports roadsters were manufactured before high interior noise and fierce competition ended production in 1966.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Zeta-Sedan",
            "generation_name": "Zeta Sedan",
            "years": {"start": 1963, "end": 1965},
            "body_styles": ["2-door micro sedan"],
            "platform": "Lightburn steel chassis with fiberglass body",
            "ancap_rating": None,
            "summary": "Villiers 324cc 2-stroke twin, front-wheel drive, independent rubber suspension, reversible ignition key for reversing.",
            "engines": [
                {
                    "engine_code": "Villiers-324-2T",
                    "name": "Villiers 324cc Air-Cooled 2-Stroke Twin",
                    "displacement_cc": 324,
                    "displacement_litres": 0.32,
                    "cylinders": 2,
                    "configuration": "Inline",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol / 2-Stroke Oil Premix",
                    "power_kw": 12.3,
                    "power_rpm": "4750",
                    "torque_nm": 28.0,
                    "torque_rpm": "2500",
                    "compression_ratio": "7.5:1",
                    "valvetrain": "Piston Port 2-Stroke",
                    "notes": "British Villiers 4T twin-cylinder; reversible Siba Dynastart system."
                }
            ],
            "badges": [
                {
                    "badge_name": "Sedan",
                    "years": {"start": 1963, "end": 1965},
                    "body_styles": ["2-door sedan"],
                    "drivetrain": "FWD",
                    "transmissions": ["4-speed sequential dog clutch manual"],
                    "msrp_aud_min": 1196,
                    "msrp_aud_max": 1290,
                    "fuel_consumption_l_100km": 5.6,
                    "kerb_weight_kg": 400,
                    "standard_features": ["Rust-free fiberglass body", "Fold-down rear bench", "Push-pull gear lever", "Reversible Dynastart ignition"],
                    "notes": "Eccentric Australian microcar."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Sedan",
                    "body_style": "2-door sedan",
                    "engine_code": "Villiers-324-2T",
                    "transmission": "4-speed sequential dog clutch manual",
                    "drivetrain": "FWD",
                    "msrp_aud": 1196,
                    "power_kw": 12.3,
                    "torque_nm": 28.0,
                    "fuel_l_100km": 5.6,
                    "towing_braked_kg": 0,
                    "notes": "Top speed 95 km/h; 50 mpg economy."
                }
            ]
        }
    ]
}

BOLWELL_NAGARI_DATA: Dict[str, Any] = {
    "make_slug": "bolwell",
    "model_slug": "nagari-mk-viii",
    "name": "Bolwell Nagari (Mk VIII)",
    "vehicle_type": "Sports Coupe / Convertible",
    "segment": "Supercar / V8 Sports",
    "years_sold_au": {"start": 1970, "end": 1974},
    "locally_built": True,
    "assembly_plants_au": [
        "Mordialloc, Victoria"
    ],
    "overview": "The Bolwell Nagari (Mk VIII) was Australia's premier bespoke production sports car, built by Campbell and Graeme Bolwell in Mordialloc, Melbourne. Featuring an ultra-rigid Y-shaped steel backbone chassis, breathtaking fiberglass coachwork, and Ford 302ci/351ci Windsor and Cleveland V8 engines, the Nagari weighed just 1,040 kg and accelerated from 0-100 km/h in 5.8 seconds, outpacing contemporary European exotics. A total of 127 units (100 coupes and 27 convertibles) were built.",
    "australian_market_notes": "Conceived after Graeme Bolwell worked with Colin Chapman at Lotus in England, the Nagari was sold as a fully built, road-compliant production car. Using an Austin 1800-derived front suspension with unequal wishbones and a live Ford rear axle with trailing arms and Panhard rod, the Nagari offered outstanding handling and explosive straight-line acceleration.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Mk-VIII",
            "generation_name": "Nagari Mk VIII",
            "years": {"start": 1970, "end": 1974},
            "body_styles": ["2-door coupe", "2-door convertible"],
            "platform": "Bolwell steel backbone chassis",
            "ancap_rating": None,
            "summary": "Bespoke Australian V8 sports car; Ford 302ci and 351ci V8s, 4-speed Toploader manual; 127 production units built.",
            "engines": [
                {
                    "engine_code": "Ford-302-Nagari",
                    "name": "Ford 302ci (4.9L) Windsor/Cleveland V8",
                    "displacement_cc": 4942,
                    "displacement_litres": 4.9,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Super)",
                    "power_kw": 179.0,
                    "power_rpm": "4800",
                    "torque_nm": 407.0,
                    "torque_rpm": "2800",
                    "compression_ratio": "9.5:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Holley 4-barrel carburettor."
                },
                {
                    "engine_code": "Ford-351-Nagari",
                    "name": "Ford 351ci (5.8L) Cleveland V8",
                    "displacement_cc": 5752,
                    "displacement_litres": 5.8,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Super)",
                    "power_kw": 224.0,
                    "power_rpm": "5400",
                    "torque_nm": 515.0,
                    "torque_rpm": "3400",
                    "compression_ratio": "10.0:1",
                    "valvetrain": "OHV 16V",
                    "notes": "Optional high-output V8; 0-100 km/h in 5.5s."
                }
            ],
            "badges": [
                {
                    "badge_name": "Coupe",
                    "years": {"start": 1970, "end": 1974},
                    "body_styles": ["2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (Ford Toploader)"],
                    "msrp_aud_min": 6500,
                    "msrp_aud_max": 7500,
                    "fuel_consumption_l_100km": 15.0,
                    "kerb_weight_kg": 1040,
                    "standard_features": ["Y-frame backbone chassis", "Hand-laid fiberglass body", "Girling 4-wheel disc brakes", "Alloy sports road wheels", "Smiths instruments"],
                    "notes": "100 coupes produced."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Coupe",
                    "body_style": "2-door coupe",
                    "engine_code": "Ford-302-Nagari",
                    "transmission": "4-speed manual (Ford Toploader)",
                    "drivetrain": "RWD",
                    "msrp_aud": 6800,
                    "power_kw": 179.0,
                    "torque_nm": 407.0,
                    "fuel_l_100km": 15.0,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 5.8s; top speed 230 km/h."
                }
            ]
        }
    ]
}

GOGGOMOBIL_DART_DATA: Dict[str, Any] = {
    "make_slug": "goggomobil-dart",
    "model_slug": "dart",
    "name": "Goggomobil Dart",
    "vehicle_type": "Roadster",
    "segment": "Micro Sports",
    "years_sold_au": {"start": 1959, "end": 1962},
    "locally_built": True,
    "assembly_plants_au": [
        "Brookvale, New South Wales"
    ],
    "overview": "The Goggomobil Dart is Australia's most famous and beloved micro-sports car. Conceived and designed by Sydney automotive pioneer Bill Buckle to bypass steep tariffs on imported fully assembled cars, the Dart combined German Hans Glas rolling chassis components with an ultra-lightweight, doorless aerodynamic fiberglass roadster body molded in Brookvale, Sydney. Standing just 1.1 meters tall and weighing only 345 kg, the Dart became an Australian cultural icon, celebrated for its playful styling and immortalized in Australian television advertisements.",
    "australian_market_notes": "To enter the car, occupants simply stepped over the scalloped fiberglass sides into bucket seats. The rear-mounted 300cc and 400cc air-cooled twin-cylinder two-stroke engines drove the rear wheels via an innovative electric pre-selector transmission. Around 700 Darts were manufactured in Sydney between 1959 and 1962.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Dart",
            "generation_name": "Goggomobil Dart",
            "years": {"start": 1959, "end": 1962},
            "body_styles": ["2-door-less open roadster"],
            "platform": "Goggomobil platform with Buckle fiberglass tub",
            "ancap_rating": None,
            "summary": "Ultralight 345kg fiberglass roadster; rear-mounted Glas 293cc and 392cc 2-stroke twins; electric pre-selector gearbox; ~700 built in Sydney.",
            "engines": [
                {
                    "engine_code": "Glas-293-2T",
                    "name": "Glas 293cc Air-Cooled 2-Stroke Twin",
                    "displacement_cc": 293,
                    "displacement_litres": 0.29,
                    "cylinders": 2,
                    "configuration": "Inline rear-mounted",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol / 2-Stroke Premix",
                    "power_kw": 11.2,
                    "power_rpm": "5000",
                    "torque_nm": 24.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "6.0:1",
                    "valvetrain": "2-Stroke",
                    "notes": "Bing carburettor; 15 bhp."
                },
                {
                    "engine_code": "Glas-392-2T",
                    "name": "Glas 392cc Air-Cooled 2-Stroke Twin",
                    "displacement_cc": 392,
                    "displacement_litres": 0.39,
                    "cylinders": 2,
                    "configuration": "Inline rear-mounted",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol / 2-Stroke Premix",
                    "power_kw": 14.9,
                    "power_rpm": "5000",
                    "torque_nm": 32.0,
                    "torque_rpm": "3900",
                    "compression_ratio": "6.5:1",
                    "valvetrain": "2-Stroke",
                    "notes": "20 bhp; top speed 105 km/h."
                }
            ],
            "badges": [
                {
                    "badge_name": "Dart 400",
                    "years": {"start": 1959, "end": 1962},
                    "body_styles": ["Open roadster"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed electric pre-selector", "4-speed manual dog clutch"],
                    "msrp_aud_min": 1270,
                    "msrp_aud_max": 1400,
                    "fuel_consumption_l_100km": 4.5,
                    "kerb_weight_kg": 345,
                    "standard_features": ["One-piece fiberglass monocoque tub", "Wraparound Plexiglas screen", "Stepped sill entry (no doors)", "Twin rear finettes"],
                    "notes": "Classic Australian cult microcar."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Dart 400",
                    "body_style": "Open roadster",
                    "engine_code": "Glas-392-2T",
                    "transmission": "4-speed electric pre-selector",
                    "drivetrain": "RWD",
                    "msrp_aud": 1350,
                    "power_kw": 14.9,
                    "torque_nm": 32.0,
                    "fuel_l_100km": 4.5,
                    "towing_braked_kg": 0,
                    "notes": "345 kg weight; 105 km/h top speed; Australian design icon."
                }
            ]
        }
    ]
}

GIOCATTOLO_DATA: Dict[str, Any] = {
    "make_slug": "giocattolo",
    "model_slug": "group-b",
    "name": "Giocattolo Group B",
    "vehicle_type": "Coupe",
    "segment": "Supercar / Exotic",
    "years_sold_au": {"start": 1986, "end": 1989},
    "locally_built": True,
    "assembly_plants_au": [
        "Caloundra, Queensland"
    ],
    "overview": "The Giocattolo Group B was an authentic Australian mid-engine supercar engineered by entrepreneur Paul Halstead and former McLaren Formula One designer Barry Lock in Caloundra, Queensland. Starting with imported Alfa Romeo Sprint bodyshells, Halstead and Lock discarded the front-drive powertrain and installed a mid-mounted Walkinshaw-fettled Holden Special Vehicles 5.0L Group A V8 (220kW/300hp), a bespoke ZF 5DS-25/2 five-speed transaxle, Kevlar/carbon-fibre composite bodywork, and Brembo racing brakes. Accelerating from 0-100 km/h in 4.5 seconds with a top speed of 260 km/h, only 15 production cars were built before funding ended in 1989.",
    "australian_market_notes": "Lock fabricated an aerospace tubular steel rear spaceframe incorporating double-wishbone suspension and cockpit-adjustable sway bars. The HSV-supplied Holden 5.0L V8 sat directly behind the driver's ears, matched to the same ZF transaxle used in the Ford GT40 and BMW M1. Weighing only 1,085 kg, the Giocattolo was faster than contemporary Ferraris and Lamborghinis.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "Group-B",
            "generation_name": "Giocattolo Group B V8",
            "years": {"start": 1986, "end": 1989},
            "body_styles": ["2-door mid-engine coupe"],
            "platform": "Alfa Romeo Sprint / Giocattolo spaceframe",
            "ancap_rating": None,
            "summary": "Australian mid-engine supercar; mid-mounted Walkinshaw HSV 5.0L V8 (220kW/400Nm), ZF 5-speed transaxle, Kevlar widebody, Brembo brakes; 15 production cars built.",
            "engines": [
                {
                    "engine_code": "Holden-HSV-5000i-Giocattolo",
                    "name": "Holden/HSV Walkinshaw 5.0L (304ci) Group A V8",
                    "displacement_cc": 4987,
                    "displacement_litres": 5.0,
                    "cylinders": 8,
                    "configuration": "V mid-mounted",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Premium)",
                    "power_kw": 220.0,
                    "power_rpm": "5400",
                    "torque_nm": 400.0,
                    "torque_rpm": "3800",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 16V with Crane Roller Rockers",
                    "notes": "Twin throttle-body EFI manifold; 300 bhp."
                }
            ],
            "badges": [
                {
                    "badge_name": "Group B",
                    "years": {"start": 1986, "end": 1989},
                    "body_styles": ["2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["ZF 5DS-25/2 5-speed manual transaxle"],
                    "msrp_aud_min": 85000,
                    "msrp_aud_max": 95000,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1085,
                    "standard_features": ["Kevlar and carbon composite body panels", "Brembo 4-piston disc brakes", "Full leather Recaro seats", "Momo steering wheel and instrumentation", "Gotti modular alloy wheels"],
                    "notes": "15 production cars built."
                }
            ],
            "configurations": [
                {
                    "badge_name": "Group B",
                    "body_style": "2-door coupe",
                    "engine_code": "Holden-HSV-5000i-Giocattolo",
                    "transmission": "ZF 5DS-25/2 5-speed manual transaxle",
                    "drivetrain": "RWD",
                    "msrp_aud": 88000,
                    "power_kw": 220.0,
                    "torque_nm": 400.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 0,
                    "notes": "0-100 km/h in 4.5s; top speed 260 km/h; Australian supercar legend."
                }
            ]
        }
    ]
}

OKA_4X4_DATA: Dict[str, Any] = {
    "make_slug": "oka",
    "model_slug": "4x4-truck",
    "name": "OKA 4x4 (LT, XT, NT)",
    "vehicle_type": "Cab Chassis / Van / Bus",
    "segment": "Heavy-Duty All-Terrain Commercial",
    "years_sold_au": {"start": 1986, "end": 2011},
    "locally_built": True,
    "assembly_plants_au": [
        "Bibra Lake, Western Australia"
    ],
    "overview": "The OKA 4x4 was an uncompromising, severe-duty all-terrain four-wheel-drive commercial truck manufactured in Bibra Lake, Perth, Western Australia. Engineered specifically to endure the most punishing outback corrugations, mine sites, and desert terrain across Australia, the OKA featured an indestructible heavy-duty perimeter box-section chassis, Dana 60 front and Dana 70 rear live drive axles, New Process transfer case, and Perkins/Cummins turbo-diesel power across LT, XT, and NT generations.",
    "australian_market_notes": "Designed for severe 5.5-tonne GVM operation where standard LandCruisers and Land Rovers suffered chassis fatigue, the OKA became the backbone of mining operations in the Pilbara, Telstra outback line maintenance in the Northern Territory, outback safari touring through the Tanami and Simpson deserts, and rural fire services. Over 500 units were manufactured.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "LT-XT-NT",
            "generation_name": "OKA 4x4 Range (LT, XT, NT)",
            "years": {"start": 1986, "end": 2011},
            "body_styles": ["Single Cab", "Dual Cab", "Multicab", "Commuter Bus", "Van"],
            "platform": "OKA heavy-gauge box-section chassis",
            "ancap_rating": None,
            "summary": "Severe-duty 4WD truck; Perkins 4.0L Phaser turbo-diesel (82kW/353Nm) and Cummins 5.9L ISBe; Dana 60/70 axles, dual-range 4WD, 5.5-tonne GVM.",
            "engines": [
                {
                    "engine_code": "Perkins-Phaser-110MT",
                    "name": "Perkins Phaser 110MT 4.0L 4-Cylinder Turbo-Diesel",
                    "displacement_cc": 3990,
                    "displacement_litres": 4.0,
                    "cylinders": 4,
                    "configuration": "Inline",
                    "aspiration": "Turbocharged",
                    "fuel_type": "Diesel",
                    "power_kw": 82.0,
                    "power_rpm": "2800",
                    "torque_nm": 353.0,
                    "torque_rpm": "1600",
                    "compression_ratio": "16.0:1",
                    "valvetrain": "OHV 8V",
                    "notes": "Legendary direct-injection industrial turbo-diesel."
                }
            ],
            "badges": [
                {
                    "badge_name": "XT Single Cab",
                    "years": {"start": 1993, "end": 2005},
                    "body_styles": ["Single Cab"],
                    "drivetrain": "4WD",
                    "transmissions": ["Spicer 5-speed manual with New Process dual-range transfer case"],
                    "msrp_aud_min": 68000,
                    "msrp_aud_max": 85000,
                    "fuel_consumption_l_100km": 15.0,
                    "kerb_weight_kg": 3100,
                    "standard_features": ["Dana 60 front drive axle", "Dana 70 rear drive axle", "Dual-range 4WD with locking hubs", "Heavy-duty semi-elliptic leaf springs", "Flat glass easily replaceable windscreen"],
                    "notes": "Indestructible Australian expedition workhorse."
                }
            ],
            "configurations": [
                {
                    "badge_name": "XT Single Cab",
                    "body_style": "Single Cab",
                    "engine_code": "Perkins-Phaser-110MT",
                    "transmission": "Spicer 5-speed manual",
                    "drivetrain": "4WD",
                    "msrp_aud": 74500,
                    "power_kw": 82.0,
                    "torque_nm": 353.0,
                    "fuel_l_100km": 15.0,
                    "towing_braked_kg": 3500,
                    "notes": "5,500 kg GVM; cross-country capability."
                }
            ]
        }
    ]
}

BRABHAM_BT62_DATA: Dict[str, Any] = {
    "make_slug": "brabham",
    "model_slug": "bt62",
    "name": "Brabham BT62 / BT62R",
    "vehicle_type": "Track / Road Hypercar",
    "segment": "Hypercar",
    "years_sold_au": {"start": 2018, "end": 2024},
    "locally_built": True,
    "assembly_plants_au": [
        "Edinburgh Parks, South Australia"
    ],
    "overview": "The Brabham BT62 and BT62R was an ultra-exclusive mid-engine hypercar manufactured in Adelaide, South Australia by Brabham Automotive, led by Le Mans winner David Brabham. Developed without turbochargers or hybrid battery weight, the BT62 featured a high-tensile tubular steel chassis with integrated carbon-kevlar monocoque safety cell, carbon-fibre body panels, and a mid-mounted naturally aspirated 5.4-litre modular V8 revving to 8,200 rpm and developing 522 kW (700 hp) and 667 Nm. Generating 1,200 kg of aerodynamic downforce with a dry weight of only 972 kg, the BT62 shattered closed-cockpit lap records at Mount Panorama Bathurst (1m 58.69s).",
    "australian_market_notes": "Hand-built in Edinburgh Parks, Adelaide, the BT62 was offered in Competition, Ultimate Track, and road-compliant BT62R specifications. The BT62R added an axle lift system, air conditioning, heated windshield, road exhaust muffler, and Australian ADR compliance.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "BT62",
            "generation_name": "Brabham BT62 & BT62R",
            "years": {"start": 2018, "end": 2024},
            "body_styles": ["2-door track hypercar", "2-door road-compliant coupe (BT62R)"],
            "platform": "Brabham carbon-composite monocoque",
            "ancap_rating": None,
            "summary": "5.4L quad-cam naturally aspirated V8 (522kW/667Nm), 6-speed Holinger sequential paddle-shift gearbox, carbon-carbon brakes, 1,200 kg downforce, 972 kg dry weight.",
            "engines": [
                {
                    "engine_code": "Brabham-5.4-NA-V8",
                    "name": "Brabham 5.4L Quad-Cam 32V Naturally Aspirated V8",
                    "displacement_cc": 5400,
                    "displacement_litres": 5.4,
                    "cylinders": 8,
                    "configuration": "V mid-mounted",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (98 / 102 Octane Racing)",
                    "power_kw": 522.0,
                    "power_rpm": "7400",
                    "torque_nm": 667.0,
                    "torque_rpm": "6200",
                    "compression_ratio": "12.0:1",
                    "valvetrain": "DOHC 32V Quad-Cam Dry Sump",
                    "notes": "Dry-sump lubrication; 700 bhp; 8,200 rpm redline; Australian-tuned."
                }
            ],
            "badges": [
                {
                    "badge_name": "BT62R (Road)",
                    "years": {"start": 2020, "end": 2024},
                    "body_styles": ["2-door coupe"],
                    "drivetrain": "RWD",
                    "transmissions": ["6-speed Holinger sequential paddle-shift"],
                    "msrp_aud_min": 1800000,
                    "msrp_aud_max": 2200000,
                    "fuel_consumption_l_100km": 18.0,
                    "kerb_weight_kg": 1050,
                    "standard_features": ["Carbon-carbon brake package", "Variable ride-height lift kit", "Goodyear Eagle F1 SuperSport tyres", "FIA carbon-composite safety cell", "Custom bespoke interior tailoring"],
                    "notes": "Road-legal Australian hypercar."
                }
            ],
            "configurations": [
                {
                    "badge_name": "BT62R (Road)",
                    "body_style": "2-door coupe",
                    "engine_code": "Brabham-5.4-NA-V8",
                    "transmission": "6-speed Holinger sequential paddle-shift",
                    "drivetrain": "RWD",
                    "msrp_aud": 1950000,
                    "power_kw": 522.0,
                    "torque_nm": 667.0,
                    "fuel_l_100km": 18.0,
                    "towing_braked_kg": 0,
                    "notes": "522kW (700hp); 1,050 kg; Australia's ultimate road-going hypercar."
                }
            ]
        }
    ]
}

HDT_VK_GROUP_A_DATA: Dict[str, Any] = {
    "make_slug": "hdt",
    "model_slug": "vk-group-a",
    "name": "HDT VK SS Group A ('Blue Meanie')",
    "vehicle_type": "Sedan",
    "segment": "Homologation Special / Muscle Car",
    "years_sold_au": {"start": 1985, "end": 1985},
    "locally_built": True,
    "assembly_plants_au": [
        "Port Melbourne, Victoria"
    ],
    "overview": "The HDT VK SS Group A, universally affectionately known as the 'Blue Meanie', is the most revered homologation muscle car in Australian touring car racing history. Built by Peter Brock's Holden Dealer Team Special Vehicles at 124 Bertie Street, Port Melbourne in 1985, the Group A was created to homologate the Commodore under international FIA Group A racing regulations. All 500 cars were painted in striking Formula Blue, featuring a de-stroked 4.9-litre (4987cc) V8 with Crane cam and roller rockers, M21 4-speed manual gearbox, Scheel velour bucket seats, and distinctive white 16-inch Aero alloy wheels.",
    "australian_market_notes": "Under FIA Group A regulations, engine capacity determined vehicle minimum racing weight. The traditional Holden 308ci (5044cc) placed the Commodore into the heavy over-5,000cc weight division. HDT and Holden engineer Larry Perkins de-stroked the engine crankshaft by 0.040 inches, reducing capacity to 4,987cc (304ci) to slip beneath the 5,000cc limit and shed over 100 kg of required racing ballast. The 500 road cars were snapped up instantly by collectors and racers.",
    "manuals": [],
    "pictures": [],
    "generations": [
        {
            "series_code": "VK-Group-A",
            "generation_name": "VK SS Group A & Group 3",
            "years": {"start": 1985, "end": 1985},
            "body_styles": ["4-door sedan"],
            "platform": "GM V-body modified by HDT",
            "ancap_rating": None,
            "summary": "500 homologation specials finished in Formula Blue; 4,987cc V8 (196kW/418Nm), Crane cam, roller rockers, Scheel interior, white 16-inch Aero wheels.",
            "engines": [
                {
                    "engine_code": "HDT-4.9L-Group-A",
                    "name": "HDT/Holden 4.9L (4987cc) Group A V8",
                    "displacement_cc": 4987,
                    "displacement_litres": 4.9,
                    "cylinders": 8,
                    "configuration": "V",
                    "aspiration": "Naturally Aspirated",
                    "fuel_type": "Petrol (Super)",
                    "power_kw": 196.0,
                    "power_rpm": "5200",
                    "torque_nm": 418.0,
                    "torque_rpm": "3600",
                    "compression_ratio": "8.8:1",
                    "valvetrain": "OHV 16V with Crane Roller Rockers and High-Lift Cam",
                    "notes": "Rochester 4-barrel carburettor; port-matched high-flow intake manifold; heavy-duty double-row timing chain."
                }
            ],
            "badges": [
                {
                    "badge_name": "SS Group A",
                    "years": {"start": 1985, "end": 1985},
                    "body_styles": ["4-door sedan"],
                    "drivetrain": "RWD",
                    "transmissions": ["4-speed manual (M21)"],
                    "msrp_aud_min": 21950,
                    "msrp_aud_max": 24500,
                    "fuel_consumption_l_100km": 14.5,
                    "kerb_weight_kg": 1340,
                    "standard_features": ["Formula Blue paint", "HDT Group A aerodynamic grille, air dam, and rear spoiler", "16x7 inch white Aero wheels", "Scheel high-bolstered velour seats", "Momo steering wheel and gear knob", "Heavy-duty Bilstein gas suspension"],
                    "notes": "500 numbered homologation cars produced."
                }
            ],
            "configurations": [
                {
                    "badge_name": "SS Group A",
                    "body_style": "4-door sedan",
                    "engine_code": "HDT-4.9L-Group-A",
                    "transmission": "4-speed manual (M21)",
                    "drivetrain": "RWD",
                    "msrp_aud": 21950,
                    "power_kw": 196.0,
                    "torque_nm": 418.0,
                    "fuel_l_100km": 14.5,
                    "towing_braked_kg": 1200,
                    "notes": "0-100 km/h in 6.9s; top speed 230 km/h; Peter Brock's most iconic road car."
                }
            ]
        }
    ]
}
