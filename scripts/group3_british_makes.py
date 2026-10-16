"""
Group 3: British makes in Australia (17 makes)
"""
from typing import Dict, Any

BRITISH_MAKES: Dict[str, Dict[str, Any]] = {
    "land-rover": {
        "make_slug": "land-rover",
        "name": "Land Rover",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1949, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "The backbone of Australian outback exploration, military transport, and luxury off-roading, with extensive local assembly at Enfield and Moorebank NSW including the iconic Australian Army Perentie 4x4 and 6x6.",
        "australian_history": "Land Rover arrived in Australia in 1949 with early Series I models deployed on the monumental Snowy Mountains Hydro-Electric Scheme, where their indestructible four-wheel drive capability established their reputation. To meet high demand and local content rules, Pressed Metal Corporation (PMC) in Enfield, Sydney began assembling CKD kits in 1956. By the 1970s and 1980s, Jaguar Rover Australia (JRA) in Moorebank, NSW was manufacturing Australian-specific Land Rovers, notably fitting the local 3.5L Rover V8 and Australian-exclusive Isuzu 4BD1 3.9-litre four-cylinder diesel engine into civilian County 110s. In the late 1980s, JRA won the Australian Army's Project Perentie contract, designing and building over 3,700 military-spec 4x4 and wide-cab 6x6 Land Rovers with galvanized chassis, leaf-spring rocker suspension, and Isuzu diesel power. Today, Land Rover Australia thrives with the modern Defender (L663), Discovery, and Range Rover luxury sub-brands.",
        "models_catalog": [
            {
                "model_slug": "defender",
                "name": "Defender / Series I-III",
                "vehicle_type": "4WD / Off-Road Utility",
                "segment": "Heavy Off-Road 4WD",
                "years_sold_au": {"start": 1949, "end": "Present"},
                "locally_built": True,
                "overview": "Australia's legendary outback and military workhorse, spanning Series I-III, County 110, Australian Army Perentie 4x4/6x6, and modern L663.",
                "generations": [
                    {"series_code": "Series-I-III", "generation_name": "Series I, II, IIA & III", "years": {"start": 1949, "end": 1984}, "body_styles": ["Short-wheelbase 88", "Long-wheelbase 109", "Cab-chassis"], "summary": "Assembled at Pressed Metal Corp Sydney; 1.6L to 2.25L petrol/diesel, 2.6L six, and Stage 1 3.5L V8."},
                    {"series_code": "County-Defender-Classic", "generation_name": "County 110 & Defender", "years": {"start": 1984, "end": 2016}, "body_styles": ["Defender 90", "Defender 110", "Defender 130 dual-cab"], "summary": "Coil-spring chassis; Isuzu 4BD1 3.9L diesel, 300Tdi, 5-cylinder Td5 (90kW), and Ford Puma 2.4/2.2 TDCi."},
                    {"series_code": "Perentie", "generation_name": "Australian Army Perentie 4x4 & 6x6", "years": {"start": 1987, "end": 2013}, "body_styles": ["4x4 Soft Top", "4x4 Survey", "6x6 Long Wheelbase", "6x6 Ambulance"], "summary": "Engineered at Moorebank NSW; galvanized chassis, naturally aspirated Isuzu 4BD1 3.9L (4x4) and turbo 4BD1T (6x6)."},
                    {"series_code": "L663", "generation_name": "Defender Modern L663", "years": {"start": 2020, "end": "Present"}, "body_styles": ["Defender 90 (3-door)", "Defender 110 (5-door)", "Defender 130 (8-seat)"], "summary": "D7x all-aluminium monocoque, D250/D300 inline-6 turbo diesel MHEV, P400 petrol, and 386kW V8."}
                ]
            },
            {
                "model_slug": "discovery",
                "name": "Discovery",
                "vehicle_type": "SUV",
                "segment": "Large 4WD SUV",
                "years_sold_au": {"start": 1991, "end": "Present"},
                "locally_built": False,
                "overview": "The family 4WD that combined Range Rover off-road ability with 7-seat suburban usability across five generations.",
                "generations": [
                    {"series_code": "Discovery-1-2", "generation_name": "Discovery Series I & II", "years": {"start": 1991, "end": 2004}, "body_styles": ["5-door 4WD"], "summary": "Live axle chassis; 3.5/3.9 V8, 200Tdi/300Tdi, and 2.5 Td5 five-cylinder diesel with ACE active anti-roll."},
                    {"series_code": "Discovery-3-4", "generation_name": "Discovery 3 & 4 (L319)", "years": {"start": 2004, "end": 2016}, "body_styles": ["5-door 4WD"], "summary": "Integrated Body Frame, Terrain Response, 2.7 TDV6, 3.0 SDV6 twin-turbo diesel, and 5.0 V8."},
                    {"series_code": "Discovery-5", "generation_name": "Discovery 5 (L462)", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door 4WD"], "summary": "Aluminium monocoque, offset rear number plate, D300 Ingenium mild-hybrid diesel, 3,500kg towing."}
                ]
            },
            {
                "model_slug": "range-rover",
                "name": "Range Rover",
                "vehicle_type": "SUV",
                "segment": "Upper Luxury 4WD",
                "years_sold_au": {"start": 1972, "end": "Present"},
                "locally_built": False,
                "overview": "The master of luxury 4WD motoring, from the hose-out interior Classic to the pinnacle of contemporary British opulence.",
                "generations": [
                    {"series_code": "Classic", "generation_name": "Range Rover Classic", "years": {"start": 1972, "end": 1996}, "body_styles": ["2-door", "4-door"], "summary": "Permanent 4WD, all-coil suspension, 3.5L/3.9L Rover V8, and luxury Vogue SE."},
                    {"series_code": "P38A-L322", "generation_name": "Range Rover P38A & L322", "years": {"start": 1995, "end": 2012}, "body_styles": ["5-door SUV"], "summary": "P38A air suspension; L322 monocoque with BMW/Jaguar V8s and monumental 4.4 TDV8 twin-turbo diesel."},
                    {"series_code": "L405-L460", "generation_name": "Range Rover L405 & L460", "years": {"start": 2013, "end": "Present"}, "body_styles": ["5-door SUV", "Long Wheelbase (LWB)"], "summary": "All-aluminium architecture, SV Autobiography, 4.4 twin-turbo V8, and 390kW/452kW mild-hybrid powertrains."}
                ]
            }
        ]
    },
    "jaguar": {
        "make_slug": "jaguar",
        "name": "Jaguar",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1946, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "Grace, pace, and space in Australia, distinguished by 1950s local assembly at Enfield NSW, a stunning 1985 Bathurst 1000 victory with the TWR XJ-S, and modern luxury saloons and SUVs.",
        "australian_history": "Jaguar cars have enthralled Australians since the XK120 sports car and Mark VII saloon of the early post-war era. Pressed Metal Corporation in Enfield, Sydney assembled Jaguar Mark VII and Mark IX saloons under CKD license in the 1950s. Jaguar's greatest Australian sporting triumph occurred at Mount Panorama on 6 October 1985, when the Tom Walkinshaw Racing (TWR) Jaguar XJ-S V12 driven by John Goss and Armin Hahne won the James Hardie 1000 outright. Sir William Lyons' saloon masterpieces—the Mark 2 and XJ6/XJ12—became fixtures of Australian professional and political society. Modern Jaguar introduced the aluminium XJ, F-Type sports car, F-Pace performance SUV, and all-electric I-Pace.",
        "models_catalog": [
            {
                "model_slug": "xj",
                "name": "XJ Series",
                "vehicle_type": "Sedan",
                "segment": "Upper Luxury Car",
                "years_sold_au": {"start": 1969, "end": "2019"},
                "locally_built": False,
                "overview": "Sir William Lyons' magnum opus, offering cat-like ride compliance, independent rear suspension, and silky XK six and V12 engines.",
                "generations": [
                    {"series_code": "Series-I-III", "generation_name": "XJ Series I, II & III", "years": {"start": 1969, "end": 1992}, "body_styles": ["4-door sedan"], "summary": "XJ6 4.2L XK inline-six, XJ12 5.3L V12, and Pininfarina-restyled Series III."},
                    {"series_code": "XJ40-X300-X308", "generation_name": "XJ40, X300 & X308", "years": {"start": 1987, "end": 2003}, "body_styles": ["4-door sedan"], "summary": "AJ6/AJ16 engines, supercharged XJR6, and retro-modern X308 with 4.0L AJ-V8 supercharged XJR."},
                    {"series_code": "X350-X351", "generation_name": "XJ Aluminium Generations", "years": {"start": 2003, "end": 2019}, "body_styles": ["4-door sedan", "Long Wheelbase"], "summary": "Lightweight bonded aluminium monocoque, Ian Callum design on X351 with 5.0L Supercharged V8 (up to 423kW XJR575)."}
                ]
            },
            {
                "model_slug": "xj-s",
                "name": "XJ-S / XJS",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Grand Tourer",
                "years_sold_au": {"start": 1976, "end": "1996"},
                "locally_built": False,
                "overview": "V12 grand tourer that achieved Australian immortality winning the 1985 Bathurst 1000 with Goss and Hahne.",
                "generations": [
                    {"series_code": "XJ-S-Classic", "generation_name": "XJ-S 5.3 V12 & 4.0", "years": {"start": 1976, "end": 1996}, "body_styles": ["2-door coupe", "Convertible", "Targa cabriolet"], "summary": "HE High Efficiency V12, 3.6L/4.0L AJ6 six-cylinder, and 6.0L V12 facelift."}
                ]
            },
            {
                "model_slug": "f-type",
                "name": "F-Type",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2013, "end": "2024"},
                "locally_built": False,
                "overview": "Spiritual successor to the E-Type, featuring lightweight aluminium architecture and roaring supercharged V6 and V8 engines.",
                "generations": [
                    {"series_code": "X152", "generation_name": "F-Type", "years": {"start": 2013, "end": 2024}, "body_styles": ["2-door coupe", "2-door convertible"], "summary": "3.0L Supercharged V6, 2.0L Turbo, and 423kW 5.0L Supercharged V8 SVR with active exhaust."}
                ]
            }
        ]
    },
    "mini": {
        "make_slug": "mini",
        "name": "MINI",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1961, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": True,
        "overview": "One of Australia's most revered nameplates, manufactured at BMC Zetland Sydney (yielding unique Australian features, 1966 Bathurst 500 class domination, and the Australian Moke) and reborn globally under BMW.",
        "australian_history": "The Mini made Australian history from the moment production commenced in 1961 at the British Motor Corporation (BMC) plant in Zetland, Sydney. Australian engineers adapted Sir Alec Issigonis' masterpiece for local conditions, engineering wind-up windows with quarter-vent lights years before the UK model adopted them, as well as unique door locks and Australian upholstery. In October 1966, the Mini Cooper S etched its name into Bathurst history: Rauno Aaltonen and Bob Holden drove a Zetland-built Cooper S to outright victory at the Gallaher 500, with Cooper S models famously sweeping the top nine outright positions! The Zetland plant also designed and manufactured the Mini Moke, converting it into the rugged Australian 'Californian' recreational utility and exporting thousands globally. Modern MINI returned to Australia in 2002 under the BMW Group, delighting drivers with go-kart handling across Hatch, Convertible, Clubman, and Countryman variants.",
        "models_catalog": [
            {
                "model_slug": "mini-classic-moke",
                "name": "Classic Mini / Cooper / Moke",
                "vehicle_type": "Hatchback / Utility / Roadster",
                "segment": "Small / Micro Car",
                "years_sold_au": {"start": 1961, "end": "Present"},
                "locally_built": True,
                "overview": "The complete Australian Mini story, from Zetland-manufactured Morris 850, Bathurst-winning Cooper S, Clubman GT, and Aussie Moke to modern BMW MINI generations.",
                "generations": [
                    {"series_code": "Morris-850-Cooper", "generation_name": "Mini Mk I & II (Australian)", "years": {"start": 1961, "end": 1970}, "body_styles": ["2-door saloon", "Van"], "summary": "Built at Zetland NSW; 848cc, 998cc Cooper, and twin-carb 1275cc Cooper S (1966 Bathurst 500 outright winner)."},
                    {"series_code": "Clubman-GT", "generation_name": "Mini Clubman & Clubman GT", "years": {"start": 1971, "end": 1978}, "body_styles": ["2-door saloon", "Van"], "summary": "Australian-exclusive Clubman GT featuring twin 1.5-inch SU carbs, Bathurst sports dash, and 10-inch Rostyle wheels."},
                    {"series_code": "Californian-Moke", "generation_name": "Australian Mini Moke", "years": {"start": 1966, "end": 1981}, "body_styles": ["Open utility / recreational"], "summary": "Designed and built at Zetland; 998cc and 1275cc Californian with 13-inch wheels, tubular bullbars, and denim trim."},
                    {"series_code": "R50-R53", "generation_name": "New MINI First Generation", "years": {"start": 2002, "end": 2006}, "body_styles": ["3-door hatch", "Convertible"], "summary": "BMW revival; 1.6L Tritec engine, Cooper, and supercharged 125kW Cooper S with bonnet scoop."},
                    {"series_code": "R56", "generation_name": "New MINI Second Generation", "years": {"start": 2007, "end": 2013}, "body_styles": ["3-door hatch", "Convertible", "Clubman", "Coupe"], "summary": "Prince 1.6L Turbo engine, Cooper S (128kW/135kW), and 155kW John Cooper Works (JCW)."},
                    {"series_code": "F56", "generation_name": "MINI Third Generation", "years": {"start": 2014, "end": "Present"}, "body_styles": ["3-door hatch", "5-door hatch", "Convertible"], "summary": "UKL platform, 1.5T 3-cylinder Cooper, 2.0T 4-cylinder Cooper S (141kW), 170kW JCW, and 225kW GP3."}
                ]
            },
            {
                "model_slug": "countryman",
                "name": "Countryman",
                "vehicle_type": "SUV",
                "segment": "Compact Luxury SUV",
                "years_sold_au": {"start": 2011, "end": "Present"},
                "locally_built": False,
                "overview": "The largest MINI, offering genuine five-seat family room, ALL4 all-wheel drive, and punchy turbo performance.",
                "generations": [
                    {"series_code": "R60", "generation_name": "Countryman First Generation", "years": {"start": 2011, "end": 2016}, "body_styles": ["5-door SUV"], "summary": "Four doors, centre rail storage, ALL4 all-wheel drive, Cooper S and JCW."},
                    {"series_code": "F60-U25", "generation_name": "Countryman 2nd & 3rd Gen", "years": {"start": 2017, "end": "Present"}, "body_styles": ["5-door SUV"], "summary": "Grown family proportions; plug-in hybrid SE ALL4, 225kW JCW, and all-electric U25 Countryman E/SE."}
                ]
            }
        ]
    },
    "aston-martin": {
        "make_slug": "aston-martin",
        "name": "Aston Martin",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1950, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Handcrafted British high-performance grand tourers, combining timeless elegance with muscular V8 and V12 symphonies in Australia.",
        "australian_history": "Aston Martin has a storied following in Australia. In the 1950s and 1960s, DB2/4, DB4, and DB5 cars were imported for wealthy Australian sports car racers and pastoralists. In the 1990s, the supercharged DB7 sparked a major commercial renaissance in Australia, followed by the Henrik Fisker-designed DB9 and V8 Vantage, built on the VH bonded aluminium architecture. Today, factory franchises operate in Sydney, Melbourne, Brisbane, Adelaide, and Perth, supplying the DB12, Vantage, and DB707 super-SUV.",
        "models_catalog": [
            {
                "model_slug": "db9-db11-db12",
                "name": "DB9 / DB11 / DB12",
                "vehicle_type": "Coupe / Volante",
                "segment": "Super Grand Tourer",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "The core V12 and twin-turbo grand tourer lineage, marrying aluminum structure with spine-tingling British pace.",
                "generations": [
                    {"series_code": "VH-DB9", "generation_name": "DB9", "years": {"start": 2004, "end": 2016}, "body_styles": ["Coupe", "Volante convertible"], "summary": "Naturally aspirated 5.9L V12 (up to 380kW), transaxle automatic, and carbon-ceramic brakes."},
                    {"series_code": "DB11-DB12", "generation_name": "DB11 & DB12", "years": {"start": 2016, "end": "Present"}, "body_styles": ["Coupe", "Volante"], "summary": "5.2L twin-turbo V12 and 4.0L twin-turbo V8, culminating in the 500kW DB12 'Super Tourer'."}
                ]
            },
            {
                "model_slug": "vantage",
                "name": "Vantage",
                "vehicle_type": "Coupe / Roadster",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2005, "end": "Present"},
                "locally_built": False,
                "overview": "Aston Martin's pure driver's sports car, spanning dry-sump 4.3L/4.7L V8, manic V12 Vantage, and modern 489kW twin-turbo warrior.",
                "generations": [
                    {"series_code": "VH-Vantage", "generation_name": "V8 & V12 Vantage (VH)", "years": {"start": 2005, "end": 2018}, "body_styles": ["Coupe", "Roadster"], "summary": "4.3L and 4.7L V8 with manual or Sportshift, and shoehorned 380kW 5.9L V12 Vantage."},
                    {"series_code": "AM6-Vantage", "generation_name": "Vantage Modern", "years": {"start": 2018, "end": "Present"}, "body_styles": ["Coupe", "Roadster"], "summary": "AMG-derived 4.0L Twin-Turbo V8 producing up to 489kW (665hp) in 2024 redesign."}
                ]
            }
        ]
    },
    "bentley": {
        "make_slug": "bentley",
        "name": "Bentley",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1948, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Crewe's master of peerless grand touring luxury and effortless torque, celebrated in Australia for W12 and V8 Continental GTs and Bentayga luxury SUVs.",
        "australian_history": "Historically sold alongside Rolls-Royce in Australia through distributors such as York Motors in Sydney and Kellow-Falkiner in Melbourne, Bentley forged its own modern destiny following Volkswagen Group's acquisition in 1998. The arrival of the 2003 Continental GT—with its twin-turbo 6.0L W12, all-wheel drive, and 300+ km/h capability—revolutionised the Australian ultra-luxury market. Today, Bentley showrooms in capital cities cater to an elite clientele seeking bespoke Mulliner finishes, Flying Spur sedans, and Bentayga SUVs.",
        "models_catalog": [
            {
                "model_slug": "continental-gt",
                "name": "Continental GT",
                "vehicle_type": "Coupe / Convertible",
                "segment": "Ultra-Luxury Grand Tourer",
                "years_sold_au": {"start": 2004, "end": "Present"},
                "locally_built": False,
                "overview": "The definitive modern Bentley, combining hand-stitched leather, knurled metal, and thunderous twin-turbo W12 and V8 engines.",
                "generations": [
                    {"series_code": "Gen-1", "generation_name": "Continental GT First Gen", "years": {"start": 2004, "end": 2011}, "body_styles": ["Coupe", "GTC convertible"], "summary": "Twin-turbo 6.0L W12 (412kW/449kW Speed), permanent Torsen all-wheel drive, and air suspension."},
                    {"series_code": "Gen-2-3-4", "generation_name": "Continental GT 2nd, 3rd & 4th Gen", "years": {"start": 2011, "end": "Present"}, "body_styles": ["Coupe", "GTC convertible"], "summary": "4.0L twin-turbo V8, 485kW W12 Speed, 48V active roll control, and 575kW Ultra Performance V8 Hybrid."}
                ]
            }
        ]
    },
    "rolls-royce": {
        "make_slug": "rolls-royce",
        "name": "Rolls-Royce",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1920, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The quintessential symbol of automotive perfection, handcrafting royal tour cars, viceregal state limousines, and modern Goodwood masterpieces.",
        "australian_history": "Rolls-Royce motor cars have graced Australian roads since the Silver Ghost era, serving as the official transport for visiting royalty, Governors-General, and prime ministers. From the 1960s Silver Cloud and Silver Shadow to the modern Goodwood era under BMW stewardship, Rolls-Royce has represented the absolute apex of luxury. Australia is an important market for the Phantom, Ghost, Wraith coupe, Cullinan luxury SUV, and the all-electric Spectre coupe.",
        "models_catalog": [
            {
                "model_slug": "phantom",
                "name": "Phantom",
                "vehicle_type": "Sedan / Coupe / Drophead",
                "segment": "Pinnacle Luxury Car",
                "years_sold_au": {"start": 2003, "end": "Present"},
                "locally_built": False,
                "overview": "The flagship of the Goodwood era, featuring coach doors, Starlight Headliner, and imperious 6.75-litre twin-turbo V12 waftability.",
                "generations": [
                    {"series_code": "Phantom-VII-VIII", "generation_name": "Phantom VII & VIII", "years": {"start": 2003, "end": "Present"}, "body_styles": ["4-door saloon", "Extended Wheelbase", "Coupe", "Drophead Coupe"], "summary": "Aluminium spaceframe, self-righting wheel centres, Magic Carpet Ride, and 6.75L twin-turbo V12."}
                ]
            },
            {
                "model_slug": "ghost",
                "name": "Ghost",
                "vehicle_type": "Sedan",
                "segment": "Upper Luxury Car",
                "years_sold_au": {"start": 2010, "end": "Present"},
                "locally_built": False,
                "overview": "Designed for owners who prefer to drive themselves as well as be chauffeured, featuring Planar suspension and all-wheel steering.",
                "generations": [
                    {"series_code": "Ghost-I-II", "generation_name": "Ghost 1st & 2nd Gen", "years": {"start": 2010, "end": "Present"}, "body_styles": ["4-door saloon", "Extended"], "summary": "Twin-turbo 6.6L and 6.75L V12, satellite-aided transmission, illuminated Pantheon grille, and Black Badge."}
                ]
            }
        ]
    },
    "mclaren": {
        "make_slug": "mclaren",
        "name": "McLaren",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 2011, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Woking's Formula 1-derived supercar manufacturer, delivering carbon-fibre MonoCell architecture, dihedral doors, and twin-turbo performance to Australian roads.",
        "australian_history": "McLaren Automotive officially entered Australia in 2011 with the launch of the MP4-12C, opening factory showrooms in Sydney and Melbourne, later expanding to Brisbane and the Gold Coast. Australian supercar enthusiasts embraced McLaren's race-bred carbon-fibre chassis, Proactive Chassis Control hydraulic suspension, and blistering twin-turbo V8 speed. Standout models include the 650S, 570S, the game-changing 720S/765LT, the hybrid Artura, and the hypercar Ultimate Series (P1, Senna, and Speedtail).",
        "models_catalog": [
            {
                "model_slug": "720s-750s",
                "name": "720S / 750S",
                "vehicle_type": "Coupe / Spider",
                "segment": "Supercar",
                "years_sold_au": {"start": 2017, "end": "Present"},
                "locally_built": False,
                "overview": "Super Series benchmark featuring eye-socket aerodynamics, 4.0-litre twin-turbo V8, and active hydraulic suspension.",
                "generations": [
                    {"series_code": "720S-750S", "generation_name": "720S & 750S", "years": {"start": 2017, "end": "Present"}, "body_styles": ["Coupe", "Spider"], "summary": "MonoCage II carbon tub; 530kW (720S) to 552kW (750S), 0-100 km/h in 2.8 seconds, and track-honed 765LT."}
                ]
            }
        ]
    },
    "lotus": {
        "make_slug": "lotus",
        "name": "Lotus",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1960, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Colin Chapman's 'simplify, then add lightness' philosophy in Australia, from classic Elan and Esprit to the Elise, Exige, and bonded aluminium Emira.",
        "australian_history": "Lotus cars have been actively raced and driven in Australia since the 1960s with the Lotus Seven, Cortina, and Europa. The mid-engine Esprit became a 1980s icon. In the late 1990s, the bonded extruded-aluminium Elise revolutionized lightweight sports car engineering, establishing a vibrant Club Lotus Australia community. Sydney-based Simply Sports Cars served as national distributor before Lotus Cars Australia unified factory operations. The 2022 Emira represents the brand's final internal-combustion sports car, ushering in the Eletre electric hyper-SUV.",
        "models_catalog": [
            {
                "model_slug": "elise-exige",
                "name": "Elise / Exige",
                "vehicle_type": "Roadster / Coupe",
                "segment": "Lightweight Sports Car",
                "years_sold_au": {"start": 1997, "end": "2021"},
                "locally_built": False,
                "overview": "Bonded aluminium featherweights weighing under 900kg, celebrated for peerless chassis telepathy and track weapon capability.",
                "generations": [
                    {"series_code": "Series-1-2-3", "generation_name": "Elise & Exige S1, S2 & S3", "years": {"start": 1997, "end": 2021}, "body_styles": ["2-door roadster", "2-door coupe"], "summary": "Rover K-series 1.8L; Toyota 1.8L VVTL-i supercharged (Exige S); S3 supercharged 3.5L Toyota V6 (up to 320kW Cup 430)."}
                ]
            },
            {
                "model_slug": "emira",
                "name": "Emira",
                "vehicle_type": "Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "Lotus's sensational final internal-combustion sports car, offering hydraulic steering, 6-speed manual V6, or AMG 2.0-litre turbo.",
                "generations": [
                    {"series_code": "Type 131", "generation_name": "Emira", "years": {"start": 2022, "end": "Present"}, "body_styles": ["2-door coupe"], "summary": "3.5L Supercharged V6 (298kW) with manual/auto, and 268kW AMG 2.0L Turbo with 8-speed DCT."}
                ]
            }
        ]
    },
    "ineos": {
        "make_slug": "ineos",
        "name": "INEOS",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 2022, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Built specifically to fill the void left by the original Land Rover Defender, INEOS chose Melbourne as its Asia-Pacific headquarters to spearhead its rugged 4WD mission in Australia.",
        "australian_history": "INEOS Automotive established its regional Asia-Pacific headquarters in Melbourne, Australia in 2021. Founder Sir Jim Ratcliffe conceived the Grenadier after Land Rover ceased production of the classic Defender. Australia was designated one of INEOS's top global target markets due to the continent's demanding outback conditions. The Grenadier features a box-section ladder chassis, Carraro beam axles front and rear, permanent four-wheel drive with triple locking differentials, and BMW 3.0-litre turbocharged inline-six petrol and diesel engines paired with ZF 8-speed automatics. The dual-cab Grenadier Quartermaster ute arrived in 2024.",
        "models_catalog": [
            {
                "model_slug": "grenadier",
                "name": "Grenadier",
                "vehicle_type": "4WD Station Wagon / Ute",
                "segment": "Heavy Off-Road 4WD",
                "years_sold_au": {"start": 2022, "end": "Present"},
                "locally_built": False,
                "overview": "No-nonsense ladder-frame 4WD engineered in Graz by Magna Steyr, built in Hambach France, and purpose-matched to Australia's harshest terrain.",
                "generations": [
                    {"series_code": "Grenadier-4x4", "generation_name": "Grenadier Station Wagon & Quartermaster", "years": {"start": 2022, "end": "Present"}, "body_styles": ["5-seat station wagon", "2-seat utility wagon", "Quartermaster dual-cab ute"], "summary": "Carraro solid beam axles, Brembo brakes, BMW B57 3.0L twin-turbo diesel (183kW/550Nm) or B58 3.0L turbo petrol (210kW/450Nm), Trialmaster and Fieldmaster editions."}
                ]
            }
        ]
    },
    "rover": {
        "make_slug": "rover",
        "name": "Rover",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1948, "end": "2005"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Distinguished British carmaker that assembled P5, P6, and SD1 models at Enfield and Zetland NSW, winning 1977 Wheels Car of the Year with the SD1 3500.",
        "australian_history": "Rover vehicles were assembled in Australia by Pressed Metal Corporation and British Leyland. The Rover P5 3-Litre and P5B 3.5 V8 were favourites of government ministers. The technologically advanced P6 2000 and 3500 featured de Dion rear suspension and inboard disc brakes. In 1977, the hatchback Rover SD1 3500 won the coveted Australian Wheels Car of the Year award. Later collaboration with Honda yielded the locally sold Rover 416i and 827 V6 before British Aerospace and BMW ownership transitions culminated in the retro-styled Rover 75. Rover ceased sales when MG Rover collapsed in 2005.",
        "models_catalog": [
            {
                "model_slug": "sd1",
                "name": "SD1 (3500 / 2600)",
                "vehicle_type": "Hatchback Sedan",
                "segment": "Large Luxury Car",
                "years_sold_au": {"start": 1977, "end": "1987"},
                "locally_built": True,
                "overview": "Ferrari Daytona-inspired five-door aerodynamic hatchback, powered by the Rover all-alloy 3.5-litre V8 and 1977 Wheels Car of the Year winner.",
                "generations": [
                    {"series_code": "SD1-Series", "generation_name": "Rover SD1", "years": {"start": 1977, "end": 1987}, "body_styles": ["5-door hatchback"], "summary": "Assembled locally at Enfield NSW; 3500 V8, 2600 six-cylinder, luxury Vanden Plas, and fuel-injected Vitesse."}
                ]
            },
            {
                "model_slug": "75",
                "name": "75",
                "vehicle_type": "Sedan / Tourer Wagon",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1999, "end": "2005"},
                "locally_built": False,
                "overview": "BMW-engineered British luxury sedan with oval instrumentation, walnut wood veneer, and KV6 engine.",
                "generations": [
                    {"series_code": "R40", "generation_name": "Rover 75", "years": {"start": 1999, "end": 2005}, "body_styles": ["4-door sedan", "Tourer wagon"], "summary": "2.0L and 2.5L KV6 quad-cam engines, 2.0 CDT BMW diesel, Club and Connoisseur trims, and rare rear-drive 4.6L V8."}
                ]
            }
        ]
    },
    "triumph": {
        "make_slug": "triumph",
        "name": "Triumph",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1948, "end": "1981"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Sporting British marque assembled in Melbourne by Australian Motor Industries (AMI) from 1959 to 1976, celebrated for the 2000/2500 saloons, Dolomite Sprint, and TR sports cars.",
        "australian_history": "Australian Motor Industries (AMI) in Port Melbourne, Victoria assembled Triumph cars under license for the Australian market. Models like the Herald, 2000, 2500TC, 2.5 PI, and Dolomite were assembled alongside Ramblers and Toyotas. The 2.5 PI was Australia's first mass-market petrol-injected production sedan, contesting the 1968 London to Sydney Marathon. The Triumph TR series (TR3, TR4, TR5, TR6, and wedge TR7) enjoyed passionate sports car sales, while the 16-valve Dolomite Sprint contested the Australian Touring Car Championship. Local assembly ended in 1976, and the brand faded globally under British Leyland in 1981.",
        "models_catalog": [
            {
                "model_slug": "2000-2500",
                "name": "2000 / 2500 / 2.5 PI",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Medium Luxury Car",
                "years_sold_au": {"start": 1964, "end": "1977"},
                "locally_built": True,
                "overview": "Michelotti-designed executive saloon assembled at Port Melbourne VIC, offering independent rear suspension and Lucas mechanical fuel injection.",
                "generations": [
                    {"series_code": "Mk-I-II", "generation_name": "Triumph 2000 & 2500 Mk I & II", "years": {"start": 1964, "end": 1977}, "body_styles": ["4-door sedan", "Estate wagon"], "summary": "2.0L inline-six, twin-carb 2500TC, 98kW 2.5 PI with Lucas injection, and plush 2500S."}
                ]
            },
            {
                "model_slug": "tr-series",
                "name": "TR Series (TR4 - TR8)",
                "vehicle_type": "Roadster / Coupe",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1953, "end": "1981"},
                "locally_built": False,
                "overview": "Rugged British roadsters that evolved from separate-chassis TR4/5/6 into the Harris Mann wedge TR7 and Rover V8 TR8.",
                "generations": [
                    {"series_code": "TR4-TR6", "generation_name": "Classic TR Series", "years": {"start": 1961, "end": 1976}, "body_styles": ["Roadster", "Surrey top"], "summary": "2.1L four-cylinder TR4A with IRS, fuel-injected 2.5L six TR5 and Karmann-styled TR6."},
                    {"series_code": "TR7-TR8", "generation_name": "Triumph TR7 & TR8", "years": {"start": 1975, "end": 1981}, "body_styles": ["Coupe", "Convertible"], "summary": "The Shape of Things to Come; 2.0L slant-four TR7 and 3.5L Rover V8 TR8."}
                ]
            }
        ]
    },
    "vauxhall": {
        "make_slug": "vauxhall",
        "name": "Vauxhall",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1920, "end": "1968"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "General Motors' British division had a foundational role in Australia: Holden built unique Australian bodies for Wyverns, Veloxes, and Crestas, and the Vauxhall Viva HB served as the direct mechanical parent of the legendary Holden Torana.",
        "australian_history": "Vauxhall was one of General Motors-Holden's primary brands in Australia prior to and alongside Holden's domestic car. Holden built bespoke Australian bodywork for Vauxhall chassis at Woodville, South Australia and Fishermans Bend, Victoria from the 1920s through the 1960s. Holden engineered unique Australian Vauxhall utilities ('coupe utilities' and 'Vagabond' open tourers) that were never sold in Britain. When GM-H introduced the Vauxhall Viva HA and HB in the 1960s, Australian engineers extensively redesigned the HB Viva with a wider track, heavy-duty suspension, and Australian styling—releasing it in 1967 as the first Holden Torana (HB). As Torana sales boomed, GM-H phased out the Vauxhall marque in Australia in 1968.",
        "models_catalog": [
            {
                "model_slug": "velox-cresta",
                "name": "Velox / Cresta",
                "vehicle_type": "Sedan / Ute / Tourer",
                "segment": "Large Family Car",
                "years_sold_au": {"start": 1948, "end": "1965"},
                "locally_built": True,
                "overview": "Six-cylinder British-designed family cars with unique Australian Holden-built body variants, including the famous Vagabond tourer and coupe utility.",
                "generations": [
                    {"series_code": "LIP-E-PA", "generation_name": "Vauxhall Velox & Cresta", "years": {"start": 1948, "end": 1965}, "body_styles": ["4-door sedan", "Coupe utility", "Vagabond tourer"], "summary": "Holden Woodville-pressed bodies, 2.3L and 2.6L overhead-valve six-cylinder engines, and dramatic PA tailfins."}
                ]
            },
            {
                "model_slug": "viva",
                "name": "Viva (HA & HB)",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Small Car",
                "years_sold_au": {"start": 1964, "end": "1968"},
                "locally_built": True,
                "overview": "The compact four-cylinder car that directly gave birth to the Holden Torana when adapted for Australian conditions by GM-H.",
                "generations": [
                    {"series_code": "HA-HB", "generation_name": "Vauxhall Viva HA & HB", "years": {"start": 1964, "end": 1968}, "body_styles": ["2-door sedan", "4-door sedan", "Wagon"], "summary": "1057cc and 1159cc four-cylinder; HB Coke-bottle styling re-engineered by Holden into the 1967 HB Torana."}
                ]
            }
        ]
    },
    "austin-morris": {
        "make_slug": "austin-morris",
        "name": "Austin / Morris (BMC Australia)",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1948, "end": "1975"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "The British Motor Corporation's Australian manufacturing titan at Victoria Park / Zetland Sydney, producing millions of Morris Minors, Austin Cambridges, Austin 1800s, and unique Australian six-cylinder Kimberley and Tasman models.",
        "australian_history": "BMC Australia established one of the largest automotive manufacturing operations in the Southern Hemisphere at Victoria Park, Zetland in Sydney. The site featured complete press shops, engine machining lines, and assembly tracks. BMC built the beloved Morris Minor, Austin A40, Cambridge, and Oxford. In the late 1960s, BMC Australia adapted Alec Issigonis' front-wheel drive Austin 1800 'Landcrab' into an Australian endurance champion—winning grueling outback trials and spawning the Australian-designed Austin 1800 Utility (ute). In 1970, Australian engineers developed the BMC X6 series: the Morris Kimberley and Tasman, powered by an Australian-designed 2.2-litre transverse overhead-cam six-cylinder engine (the E6). Financial headwinds under British Leyland led to the Zetland factory closure in 1974-75.",
        "models_catalog": [
            {
                "model_slug": "morris-minor",
                "name": "Morris Minor",
                "vehicle_type": "Sedan / Ute / Tourer",
                "segment": "Small Car",
                "years_sold_au": {"start": 1949, "end": "1963"},
                "locally_built": True,
                "overview": "Sir Alec Issigonis' masterpiece, assembled in Sydney in huge numbers with local body pressings and beloved by generations of Australians.",
                "generations": [
                    {"series_code": "Series-MM-II-1000", "generation_name": "Morris Minor", "years": {"start": 1949, "end": 1963}, "body_styles": ["2-door sedan", "4-door sedan", "Tourer convertible", "Coupe utility", "Panel van"], "summary": "918cc side-valve to 803cc, 948cc, and 1098cc A-series overhead-valve engines; rack and pinion steering."}
                ]
            },
            {
                "model_slug": "austin-1800",
                "name": "Austin 1800 (Landcrab & Ute)",
                "vehicle_type": "Sedan / Utility",
                "segment": "Medium / Large Family Car",
                "years_sold_au": {"start": 1965, "end": "1971"},
                "locally_built": True,
                "overview": "Vast interior space and Hydrolastic suspension, adapted with heavy-duty Australian dust sealing and transformed into the Aussie Austin 1800 ute.",
                "generations": [
                    {"series_code": "Mk-I-II", "generation_name": "Austin 1800 Mk I & II", "years": {"start": 1965, "end": 1971}, "body_styles": ["4-door sedan", "Coupe utility"], "summary": "1.8L B-series four-cylinder; 1965 Wheels Car of the Year; uniquely Australian-designed coupe utility built at Zetland."}
                ]
            },
            {
                "model_slug": "kimberley-tasman",
                "name": "Morris Kimberley / Tasman (BMC X6)",
                "vehicle_type": "Sedan",
                "segment": "Large Family Car",
                "years_sold_au": {"start": 1970, "end": "1973"},
                "locally_built": True,
                "overview": "Australian-designed and built family car featuring the world's first transverse-mounted overhead-cam six-cylinder engine (2.2L E6).",
                "generations": [
                    {"series_code": "X6", "generation_name": "BMC X6 Kimberley & Tasman", "years": {"start": 1970, "end": 1973}, "body_styles": ["4-door sedan"], "summary": "Tasman (single carb, 76kW) and Kimberley (twin SU carbs, 86kW), front-wheel drive, Hydrolastic suspension."}
                ]
            }
        ]
    },
    "hillman-humber-sunbeam": {
        "make_slug": "hillman-humber-sunbeam",
        "name": "Hillman / Humber / Sunbeam (Rootes Group)",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1946, "end": "1979"},
        "currently_sold_au": False,
        "local_manufacturer": True,
        "overview": "Rootes Group Australia manufactured Hillmans, Humbers, and Sunbeams at Salmon Street, Port Melbourne, scoring an immortal international victory in the 1968 London to Sydney Marathon with an Australian-built Hillman Hunter.",
        "australian_history": "Rootes Group established Australian assembly operations at Salmon Street, Port Melbourne in 1946. Hillman Minx, Super Minx, and the rear-engine Hillman Imp were suburban driveway staples. The stately Humber Super Snipe served as premier government limousines. In 1968, an Australian-assembled Hillman Hunter driven by Andrew Cowan, Colin Malkin, and Brian Coyle famously won the 10,000-mile London to Sydney Marathon outright, shocking factory teams worldwide. Chrysler Australia acquired Rootes Group in 1965-66, integrating the Port Melbourne plant and continuing Hunter and Sunbeam production before transitioning the facility to Chrysler Valiant Galant assembly.",
        "models_catalog": [
            {
                "model_slug": "hillman-hunter",
                "name": "Hillman Hunter / Arrow",
                "vehicle_type": "Sedan / Wagon",
                "segment": "Medium Family Car",
                "years_sold_au": {"start": 1967, "end": "1973"},
                "locally_built": True,
                "overview": "Assembled at Port Melbourne VIC, celebrated for winning the grueling 1968 London to Sydney Marathon.",
                "generations": [
                    {"series_code": "Arrow-Series", "generation_name": "Hillman Hunter", "years": {"start": 1967, "end": 1973}, "body_styles": ["4-door sedan", "Safari wagon"], "summary": "1725cc five-bearing engine with alloy cylinder head, Hunter GL, Safari wagon, and Hustler sports sedan."}
                ]
            },
            {
                "model_slug": "hillman-minx",
                "name": "Hillman Minx",
                "vehicle_type": "Sedan / Wagon / Ute",
                "segment": "Small / Medium Car",
                "years_sold_au": {"start": 1946, "end": "1967"},
                "locally_built": True,
                "overview": "One of Australia's most ubiquitous post-war family cars, assembled in Melbourne with local coupe utility derivatives.",
                "generations": [
                    {"series_code": "Phase-I-Series-VI", "generation_name": "Hillman Minx & Super Minx", "years": {"start": 1946, "end": 1967}, "body_styles": ["4-door sedan", "Coupe utility", "Estate wagon"], "summary": "Side-valve 1185cc to overhead-valve 1390cc, 1494cc, and 1592cc engines, including Audax Series."}
                ]
            }
        ]
    },
    "morgan": {
        "make_slug": "morgan",
        "name": "Morgan",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1955, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "Handcrafted traditional British sports cars built with ash wood subframes in Malvern Link, imported to Australia for discerning purists.",
        "australian_history": "Morgan sports cars have been imported to Australia by dedicated specialist agents—most notably Morgan Cars Australia in Melbourne—since the 1950s. Revered for hand-beaten aluminium panels over English ash timber frames, the Plus 4, 4/4, Rover V8-powered Plus 8, and quirky 3 Wheeler have maintained a passionate following and ADR road-legal compliance.",
        "models_catalog": [
            {
                "model_slug": "plus-4-plus-8",
                "name": "Plus 4 / Plus 8",
                "vehicle_type": "Roadster",
                "segment": "Bespoke Classic Sports Car",
                "years_sold_au": {"start": 1955, "end": "Present"},
                "locally_built": False,
                "overview": "Timeless British roadsters spanning Triumph four-cylinders, 3.5L/3.9L Rover V8, and modern BMW turbocharged powertrains.",
                "generations": [
                    {"series_code": "Classic-Morgan", "generation_name": "Morgan Plus 4 & Plus 8 Classic", "years": {"start": 1955, "end": "2018"}, "body_styles": ["2-door roadster"], "summary": "Steel ladder chassis, ash frame, Rover V8, Ford Zetec/Duratec four-cylinder engines."},
                    {"series_code": "CX-Generation", "generation_name": "Plus Four & Plus Six (CX)", "years": {"start": 2020, "end": "Present"}, "body_styles": ["2-door roadster"], "summary": "CX bonded aluminium chassis, BMW 2.0L Turbo (Plus Four) and 3.0L Turbo inline-6 (Plus Six)."}
                ]
            }
        ]
    },
    "caterham": {
        "make_slug": "caterham",
        "name": "Caterham",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1985, "end": "Present"},
        "currently_sold_au": True,
        "local_manufacturer": False,
        "overview": "The pure evolution of Colin Chapman's Lotus Seven, delivering peerless power-to-weight track performance and road legality in Australia.",
        "australian_history": "Caterham acquired the rights to the Lotus Seven in 1973 and has been imported into Australia as turn-key and enthusiast road cars since the mid-1980s. Caterham Cars Australia supplies models engineered for ADR compliance, from the Suzuki-turbocharged Seven 160/170 to the manic Ford Duratec-powered Seven 485 and 620R. They remain the gold standard for club motorsport and tarmac rally hillclimbs.",
        "models_catalog": [
            {
                "model_slug": "seven",
                "name": "Seven",
                "vehicle_type": "Roadster",
                "segment": "Track / Sports Car",
                "years_sold_au": {"start": 1985, "end": "Present"},
                "locally_built": False,
                "overview": "Lightweight open-wheel roadster weighing just 500-600kg, offering unmatched cornering G-forces and mechanical feedback.",
                "generations": [
                    {"series_code": "Seven-Series", "generation_name": "Caterham Seven", "years": {"start": 1985, "end": "Present"}, "body_styles": ["2-door open roadster"], "summary": "Tubular steel spaceframe, De Dion rear axle, Rover K-series, and Ford Sigma/Duratec engines up to 177kW in Seven 485."}
                ]
            }
        ]
    },
    "tvr": {
        "make_slug": "tvr",
        "name": "TVR",
        "country_of_origin": "United Kingdom",
        "years_active_au": {"start": 1988, "end": "2006"},
        "currently_sold_au": False,
        "local_manufacturer": False,
        "overview": "Blackpool's outrageous, lightweight fibreglass beasts—no ABS, no traction control, pure thunderous Rover V8 and Speed Six power.",
        "australian_history": "TVR was imported into Australia in low volumes by enthusiasts and specialist agents in Sydney and Melbourne through the 1980s and 1990s. Models like the Chimaera, Griffith 500, and Speed Six-powered Tuscan captured admiration for their outrageous power-to-weight ratios, tubular steel backbone chassis, and aggressive exhaust roar. Production ended globally in 2006, leaving an indelible cult legacy.",
        "models_catalog": [
            {
                "model_slug": "chimaera-griffith",
                "name": "Chimaera / Griffith",
                "vehicle_type": "Roadster",
                "segment": "Sports Car",
                "years_sold_au": {"start": 1992, "end": "2003"},
                "locally_built": False,
                "overview": "V8 roadsters featuring hand-laid fibreglass bodies, bespoke leather cabins, and tuned Rover 4.0L, 4.5L, and 5.0L V8s.",
                "generations": [
                    {"series_code": "V8-Roadsters", "generation_name": "TVR Chimaera & Griffith", "years": {"start": 1992, "end": "2003"}, "body_styles": ["2-door roadster"], "summary": "Tubular spaceframe, double-wishbone suspension, dry-sump 5.0L V8 producing 254kW in a 1,060kg roadster."}
                ]
            }
        ]
    }
}
