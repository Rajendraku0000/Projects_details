import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("cars.csv")

# Data_cleaning 

df['name']=df['name'].str.split().str.slice(start=0,stop=3).str.join(' ')
# df["company"]=df["name"].str.split(" ",expand=True)[0]


name=['Maruti 800 AC', 'Maruti Gypsy E', 'Mahindra Jeep CL',
       'Mahindra Jeep MM', 'Maruti Esteem AX', 'Maruti 800 Std',
       'Maruti Omni 5', 'Maruti Zen LXI', 'Mercedes-Benz E-Class 230',
       'Honda City 1.3', 'Maruti Zen LX', 'Hyundai Santro GLS',
       'Maruti Esteem VX', 'Mahindra Jeep Classic', 'Hyundai Accent GLE',
       'Maruti Gypsy King', 'Maruti 800 DX', 'Maruti Wagon R',
       'Ford Ikon 1.4', 'Maruti Zen VXI', 'Maruti Alto LX',
       'Maruti Alto LXi', 'Hyundai Santro LP', 'Hyundai Santro LE',
       'Maruti 800 EX', 'Mercedes-Benz E-Class 220', 'Maruti Omni E',
       'Maruti Zen VX', 'Mahindra Bolero DI', 'Toyota Qualis FS',
       'Tata Sumo SE', 'Maruti Zen LXi', 'Tata Indica LSI',
       'Daewoo Matiz SD', 'Hyundai Santro LS', 'Hyundai Accent CRDi',
       'Ambassador Classic 2000', 'Maruti Alto VXi', 'OpelCorsa 1.4 GL',
       'Skoda Octavia Ambiente', 'Maruti Zen D', 'Tata Indica DLX',
       'Fiat Palio D', 'Honda City VTEC', 'Maruti Alto LXI',
       'Hyundai Santro Xing', 'Toyota Corolla H3', 'Ford Endeavour 4x4',
       'Skoda Octavia Classic', 'Honda City 1.5', 'Tata Indica LXI',
       'Mahindra Scorpio 2.6', 'Mahindra Scorpio VLX',
       'Hyundai Accent GLS', 'OpelCorsa 1.6Gls', 'Maruti Zen VXi',
       'Ford Endeavour 4x2', 'Ford Endeavour 2.5L', 'Maruti Esteem Lxi',
       'Tata Indica DLS', 'Hyundai Getz GLS', 'Maruti Swift 1.3',
       'Hyundai Santro GS', 'Chevrolet Tavera LS', 'Tata Indica DLE',
       'Toyota Innova 2.5', 'Chevrolet Optra 1.6', 'Ford Fusion 1.6',
       'Maruti Esteem Vxi', 'Ford Ikon 1.8', 'Hyundai Getz GLX',
       'Hyundai Santro AT', 'Ford Ikon 1.6', 'Ford Ikon 1.3',
       'Ambassador CLASSIC 1500', 'Toyota Corolla H2', 'Maruti Alto STD',
       'Ford Fiesta Classic', 'Tata Sumo GX', 'Hyundai Getz GL',
       'Maruti Baleno Vxi', 'Mahindra Bolero SLX', 'Mahindra Scorpio REV',
       'Ford Ikon 1.3L', 'Skoda Laura L', 'Maruti Alto 800',
       'Chevrolet Tavera LT', 'Mahindra Jeep CJ', 'Hyundai Elantra CRDi',
       'Tata Indica DL', 'Ford Fiesta 1.6', 'Honda Civic 1.8',
       'Toyota Corolla AE', 'Tata Indica GLS', 'Tata Indigo GLX',
       'Hyundai Accent GLX', 'Chevrolet Aveo 1.6', 'Hyundai Tucson CRDi',
       'BMW 7 Series', 'Maruti Swift VXI', 'Maruti Omni LPG',
       'Hyundai Sonata AT', 'Hyundai Sonata 2.4L', 'BMW 5 Series',
       'Toyota Camry Hybrid', 'Tata Indigo Classic', 'Maruti SX4 Vxi',
       'Maruti Swift Vdi', 'Maruti SX4 Zxi', 'Chevrolet Tavera Neo',
       'Maruti Swift VDI', 'Hyundai Verna CRDi', 'Maruti Zen Estilo',
       'Tata Indigo LS', 'Hyundai Getz GLE', 'Ford Endeavour Hurricane',
       'Hyundai Verna SX', 'Hyundai Verna XXi', 'Toyota Corolla H6',
       'Skoda Laura Ambiente', 'Honda Accord VTi-L', 'Tata New Safari',
       'Mercedes-Benz New C-Class', 'Mahindra Bolero SLE',
       'Mahindra Scorpio SLX', 'Mitsubishi Montero 3.2',
       'Maruti Omni CNG', 'Mahindra Renault Logan', 'Ford Fiesta 1.4',
       'Chevrolet Aveo 1.4', 'Maruti Grand Vitara', 'Hyundai Verna i',
       'Maruti Swift ZXI', 'Mercedes-Benz E-Class 280',
       'Chevrolet Aveo U-VA', 'Fiat Palio 1.2', 'Hyundai Getz 1.3',
       'Chevrolet Spark 1.0', 'Chevrolet Captiva LT',
       'Hyundai i10 Sportz', 'Hyundai i10 Magna', 'Ford Endeavour XLT',
       'Maruti Swift Dzire', 'Maruti Omni BSIII', 'Mahindra Scorpio M2DI',
       'Hyundai i10 Era', 'Maruti A-Star Lxi', 'Maruti Swift Ldi',
       'Hyundai Verna 1.6', 'Toyota Corolla Altis', 'Maruti Swift VDi',
       'Tata Indigo TDI', 'Hyundai Getz 1.5', 'Toyota Camry M/t',
       'Fiat 500 Lounge', 'Maruti Swift LXi', 'Volkswagen Jetta 1.9',
       'Maruti Swift VXi', 'Mahindra Scorpio VLS', 'Tata Indica Vista',
       'Tata Indigo LX', 'Tata Indigo GLE', 'Tata Indigo GLS',
       'Audi A6 2.8', 'Audi Q7 35', 'Mahindra Scorpio LX',
       'Hyundai i20 Asta', 'Mahindra Xylo E4', 'Tata Indica V2',
       'Honda Jazz S', 'Hyundai i20 1.4', 'Maruti A-Star Vxi',
       'Maruti Swift Glam', 'Honda Accord 2.4', 'Mahindra Xylo D2',
       'Chevrolet Optra Magnum', 'Maruti Ritz LXI',
       'Mahindra Scorpio SLE', 'Toyota Corolla Executive',
       'Tata Manza Aura', 'Skoda Superb Elegance', 'Audi A8 L',
       'Skoda Laura 1.9', 'Maruti SX4 ZXI', 'Tata Sumo Victa',
       'Maruti 800 DUO', 'Maruti Ritz VDi', 'Tata Sumo LX',
       'Chevrolet Beat Diesel', 'Mahindra Xylo E8', 'Fiat Grande Punto',
       'Tata Nano Std', 'Tata Spacio SA', 'Toyota Fortuner 3.0',
       'Mahindra Xylo E6', 'Maruti Ritz VXI', 'Mercedes-Benz E-Class E',
       'Hyundai Sonata CRDi', 'Jaguar XJ 5.0', 'Ford Figo Diesel',
       'Skoda Fabia 1.2L', 'Chevrolet Cruze LTZ', 'Hyundai i20 Sportz',
       'Chevrolet Beat LT', 'Ford Figo Titanium',
       'Volkswagen Polo Petrol', 'Hyundai i20 Magna', 'Ford Figo Petrol',
       'Honda City VX', 'Tata Nano Lx', 'Skoda Laura Elegance',
       'Volkswagen Polo Diesel', 'Volkswagen Passat 1.8',
       'Hyundai Accent Executive', 'Mahindra Xylo D4',
       'Hyundai Verna Transform', 'Maruti Alto K10', 'Fiat Punto 1.2',
       'Toyota Innova 2.0', 'Skoda Superb 1.8', 'Honda Jazz Select',
       'Maruti Ritz VXi', 'Maruti Alto Green', 'Hyundai i20 1.2',
       'Chevrolet Beat LS', 'Fiat Punto 1.3', 'Audi Q5 2.0',
       'Maruti Eeco 5', 'Fiat Linea Emotion', 'Nissan X-Trail SLX',
       'Fiat Linea 1.3', 'Audi A6 2.7', 'Tata Xenon XT',
       'Mahindra Xylo Celebration', 'Tata Indigo CR4', 'Tata Nano Cx',
       'Fiat Punto 1.4', 'Land Rover Range', 'Fiat Linea T',
       'Tata Manza Aqua', 'Skoda Superb Ambition', 'Hyundai i10 Asta',
       'Skoda Yeti Ambition', 'BMW X1 sDrive', 'Ford Endeavour Titanium',
       'Volkswagen Jetta 2.0', 'Volkswagen Vento Diesel',
       'Toyota Etios VD', 'Toyota Etios V', 'Volkswagen Vento Petrol',
       'Volkswagen Polo 1.5', 'Maruti SX4 ZDI', 'Ford Fiesta Titanium',
       'Honda Jazz VX', 'Ford Endeavour 3.0L', 'Ford Fiesta 1.5',
       'Maruti Swift LXI', 'Toyota Innova Crysta', 'Nissan Micra Diesel',
       'Tata Manza ELAN', 'Maruti SX4 VDI', 'Toyota Etios VX',
       'Tata Indigo CS', 'Mitsubishi Pajero 2.8', 'Hyundai Verna 1.4',
       'Mercedes-Benz E-Class E250', 'Toyota Etios GD', 'Nissan Micra XL',
       'BMW X1 sDrive20d', 'Maruti Ritz LDi', 'Volkswagen Vento 1.0',
       'Ford Classic 1.6', 'Volkswagen Vento IPL', 'Skoda Fabia 1.2',
       'Honda City V', 'Audi A4 2.0', 'Maruti Ritz LXi',
       'Chevrolet Captiva 2.0L', 'Mahindra Verito 1.5', 'Hyundai EON Era',
       'Fiat Linea Active', 'Hyundai Santa Fe', 'Mahindra Thar 4X2',
       'Tata Winger Deluxe', 'Chevrolet Cruze LT', 'Mahindra Quanto C8',
       'Hyundai EON Magna', 'Renault Duster 110PS',
       'Maruti SX4 Celebration', 'Mitsubishi Outlander 2.4',
       'Mahindra XUV500 W8', 'Toyota Etios Liva', 'Mahindra XUV500 W6',
       'Honda Brio E', 'Honda Brio S', 'Hyundai EON LPG', 'Jaguar XF 5.0',
       'Tata Venture EX', 'Skoda Rapid 1.6', 'Hyundai EON 1.0',
       'Maruti Ertiga ZDI', 'Volkswagen Jetta 2.0L',
       'Volkswagen Polo 1.0', 'Volkswagen Vento 1.5',
       'Mitsubishi Pajero Sport', 'Honda City S', 'Nissan Sunny XL',
       'Nissan Sunny Diesel', 'Jaguar XF 3.0', 'Volkswagen Vento New',
       'Hyundai EON D', 'Renault Fluence 1.5', 'Renault Koleos 2.0',
       'Maruti Ertiga VDI', 'Mahindra Quanto C6', 'Tata Nano LX',
       'Maruti Omni MPI', 'Renault Duster 85PS', 'Renault Pulse RxZ',
       'Maruti Swift ZDi', 'Mahindra Scorpio EX', 'Hyundai EON Sportz',
       'Ford Fiesta Diesel', 'Ford Fiesta Petrol', 'Ford Figo 1.2P',
       'Honda Brio 1.2', 'Honda Brio V', 'Volkswagen Vento 1.6',
       'Volvo XC60 D3', 'Tata Manza Club', 'Audi A4 1.8',
       'Ambassador Grand 1800', 'Mahindra Xylo E9', 'Maruti A-Star AT',
       'Skoda Superb LK', 'Tata Aria Pleasure', 'Audi Q3 2.0',
       'Maruti Swift LDI', 'Chevrolet Enjoy TCDi', 'Audi A6 2.0',
       'BMW 3 Series', 'Mahindra Bolero 2011-2019', 'Audi A8 4.2',
       'Volkswagen Jetta 1.4', 'Honda Amaze VX', 'Chevrolet Enjoy 1.3',
       'Renault Scala RxL', 'Maruti Ertiga VXI', 'Hyundai Grand i10',
       'Tata Nano STD', 'Chevrolet Sail Hatchback', 'Ford EcoSport 1.5',
       'Honda Amaze EX', 'Audi A4 3.0', 'Tata Safari Storme',
       'Mahindra Verito Vibe', 'Volkswagen Vento Magnific',
       'Ford Ecosport 1.0', 'Nissan Terrano XV', 'Ford Ecosport 1.5',
       'Honda Amaze S', 'Honda City E', 'Tata Nano CX', 'Tata Sumo Gold',
       'Mahindra Quanto C4', 'Fiat Linea Dynamic', 'Mahindra Thar 4X4',
       'Honda City Corporate', 'Volkswagen Polo SR', 'Maruti Omni 8',
       'Nissan Micra Active', 'Mercedes-Benz B Class',
       'Tata Safari DICOR', 'Maruti Ritz VDI', 'Renault Duster Petrol',
       'Tata Indigo Grand', 'Honda Amaze E', 'Maruti Eeco Smiles',
       'Maruti Swift Star', 'Ford Classic 1.4', 'Nissan Terrano XL',
       'Renault Scala Diesel', 'Chevrolet Sail 1.3',
       'Skoda Octavia Elegance', 'Nissan Terrano XE', 'Jaguar XF 2.2',
       'Mahindra Scorpio 1.99', 'Honda City i', 'Hyundai i20 2015-2017',
       'Skoda Rapid 1.5', 'Honda Mobilio V', 'Chevrolet Sail 1.2',
       'Honda City i-DTEC', 'Maruti Estilo LXI', 'Toyota Fortuner 4x4',
       'Mercedes-Benz GL-Class 350', 'Tata Zest Revotron', 'Audi A4 New',
       'Mercedes-Benz M-Class ML', 'Hyundai Xcent 1.1',
       'Honda City i-VTEC', 'Maruti Ertiga ZXI', 'Maruti Swift 1.2',
       'Renault Duster RXL', 'Maruti Ciaz ZDi', 'Tata Aria Pure',
       'Force One EX', 'Nissan Evalia XV', 'Maruti Eeco 7',
       'Mahindra Scorpio S4', 'Chevrolet Beat PS', 'Honda Brio Exclusive',
       'Maruti Celerio VXI', 'Hyundai Xcent 1.2', 'Toyota Fortuner 4x2',
       'Volvo XC60 D5', 'Volkswagen Polo 1.2', 'Tata Nano Twist',
       'Datsun GO T', 'Chevrolet Sail LS', 'Maruti Ciaz VXi',
       'Mahindra Scorpio S10', 'Honda Brio VX', 'Mahindra Thar CRDe',
       'Hyundai Creta 1.6', 'Fiat Avventura MULTIJET', 'Ford Figo Aspire',
       'Maruti Ciaz VDi', 'Tata Zest Quadrajet', 'Mahindra Bolero Power',
       'Maruti Baleno Sigma', 'Datsun GO A', 'Datsun GO Plus',
       'Maruti Ertiga BSIV', 'Renault KWID RXT', 'Maruti S-Cross Zeta',
       'Renault Pulse RxL', 'Mahindra Scorpio S6', 'Fiat Linea Classic',
       'Toyota Etios Cross', 'Nissan Sunny XV', 'Maruti Ciaz ZXi',
       'Renault Lodgy 85PS', 'Honda Jazz 1.5', 'Maruti Swift ZDI',
       'Audi A4 35', 'Hyundai Elantra SX', 'Ford Figo 1.5D',
       'Mahindra Scorpio S2', 'Mahindra XUV500 AT', 'Mahindra XUV500 W10',
       'Maruti SX4 S', 'Maruti Ertiga SHVS', 'Hyundai i20 Active',
       'Honda Amaze SX', 'Hyundai Elite i20', 'Honda Mobilio S',
       'Maruti Celerio ZDi', 'Maruti Baleno Alpha',
       'Mahindra Ingenio CRDe', 'Ford Aspire Titanium',
       'Toyota Etios VXD', 'Mahindra TUV 300', 'Maruti Baleno Delta',
       'Audi Q5 3.0', 'Tata Bolt Revotron', 'Maruti Swift DDiS',
       'Maruti Celerio VDi', 'Tata Nano XM', 'Hyundai Creta 1.4',
       'Tata Bolt Quadrajet', 'Volkswagen Vento Celeste',
       'Maruti Vitara Brezza', 'Renault KWID RXL', 'Mahindra KUV 100',
       'Maruti Baleno Zeta', 'Ford Endeavour 3.2', 'Land Rover Discovery',
       'Mahindra Bolero B6', 'Mahindra Xylo H4',
       'Ford Freestyle Titanium', 'Mahindra Thar DI',
       'Mahindra NuvoSport N8', 'Datsun RediGO S', 'Renault KWID 1.0',
       'Tata Tiago 2019-2020', 'Tata Tiago 1.05', 'Honda BR-V i-DTEC',
       'Toyota Etios 1.5', 'Tata Tiago 1.2', 'Honda Jazz 1.2',
       'Tata Tiago XT', 'Maruti Ciaz VDI', 'Ford Figo Trend',
       'Datsun RediGO T', 'Volkswagen CrossPolo 1.2', 'Toyota Etios 1.4',
       'Renault KWID RXE', 'Maruti S-Cross Alpha', 'Audi RS7 2015-2019',
       'Mercedes-Benz GLS 2016-2020', 'Fiat Punto EVO',
       'Maruti Celerio ZXI', 'Toyota Fortuner 2.7',
       'Maruti Celerio Green', 'Mercedes-Benz S-Class S',
       'Datsun RediGO 1.0', 'Maruti Swift VVT', 'Maruti S-Cross Facelift',
       'Volkswagen Ameo 1.5', 'Mahindra Scorpio S11', 'Maruti Swift ZXi',
       'Mahindra Supro VX', 'Toyota Fortuner 2.8', 'Hyundai Tucson 2.0',
       'Hyundai Verna VTVT', 'Volkswagen Polo GTI', 'Tata Hexa XT',
       'Tata Hexa XM', 'Maruti Ciaz 1.4', 'Renault KWID Climber',
       'Tata Hexa XTA', 'Maruti Ignis 1.2', 'Toyota Camry 2.5',
       'Honda Mobilio E', 'Renault Captur 1.5',
       'Volkswagen Polo 2015-2019', 'Tata Nexon 1.5', 'Tata Nexon 1.2',
       'Ford Figo 1.5P', 'Honda WR-V i-DTEC', 'Renault Lodgy Stepway',
       'Honda BRV i-VTEC', 'Mahindra Bolero B4', 'Renault KWID AMT',
       'Tata Tigor 1.2', 'Honda BR-V i-VTEC', 'Skoda Rapid Monte',
       'Honda BRV i-DTEC', 'Honda WR-V i-VTEC', 'Maruti S-Cross Sigma',
       'Jeep Compass 2.0', 'Audi Q3 35', 'Volvo XC 90', 'Ford Figo 1.5',
       'Maruti Omni Maruti', 'Maruti Ciaz 1.3',
       'Mercedes-Benz E-Class Exclusive', 'Volvo V40 D3',
       'Mahindra Marazzo M8', 'Mahindra Scorpio S7',
       'Mahindra XUV500 W11', 'Fiat Avventura Urban',
       'Mercedes-Benz C-Class Progressive', 'Maruti Swift AMT',
       'Tata Tiago XZA', 'Mahindra Marazzo M4', 'Mahindra XUV500 W5',
       'Audi A4 30', 'Honda Amaze V', 'Honda CR-V Diesel',
       'Datsun redi-GO AMT', 'Toyota Yaris G', 'Maruti Ignis 1.3',
       'Volkswagen Ameo 1.2', 'Mahindra XUV500 W7', 'Isuzu D-Max V-Cross',
       'Hyundai Santro Asta', 'Maruti Ciaz Sigma',
       'Mahindra Scorpio BSIV', 'Hyundai Elantra 2.0', 'Maruti Ciaz S',
       'Maruti Baleno RS', 'Datsun RediGO AMT', 'Mahindra Xylo H8',
       'Honda City Edge', 'Hyundai Venue SX', 'Jeep Compass 1.4',
       'Mahindra XUV300 W8', 'Tata Tiago NRG', 'Hyundai Santro Era',
       'Hyundai Santro Magna', 'BMW X5 xDrive', 'Maruti Ciaz Zeta',
       'Maruti Celerio LXI', 'Mahindra Alturas G4',
       'Ford Freestyle Trend', 'Honda Jazz V', 'MG Hector Sharp',
       'Hyundai Santro Sportz', 'Maruti S-Presso VXI', 'Tata Harrier XZ',
       'Nissan Kicks XV', 'Mahindra Marazzo M2', 'Renault Triber RXT',
       'Maruti Celerio X', 'Nissan Kicks XL', 'Kia Seltos HTK',
       'Maruti Eeco CNG', 'Maruti S-Cross Delta', 'Datsun RediGO SV',
       'Mahindra Scorpio S9', 'MG Hector Smart', 'Volkswagen Polo GT',
       'Maruti Ertiga 1.5', 'Ford Endeavour 2.2', 'Audi A5 Sportback',
       'Ford Ecosport Thunder', 'Tata Altroz XZ', 'Ford Ecosport Sports',
       'Tata Altroz XE', 'Mahindra Scorpio S5', 'Tata Harrier XE']


seller_type=['Individual', 'Dealer', 'Trustmark Dealer']

df["transmission"].unique()


transmission=['Manual', 'Automatic']

df["owner"].unique()

owner=['Fourth & Above Owner', 'Second Owner', 'First Owner',
       'Third Owner', 'Test Drive Car']

company=['Maruti', 'Mahindra', 'Mercedes-Benz', 'Honda', 'Hyundai', 'Ford',
       'Toyota', 'Tata', 'Daewoo', 'Ambassador', 'OpelCorsa', 'Skoda',
       'Fiat', 'Chevrolet', 'BMW', 'Mitsubishi', 'Volkswagen', 'Audi',
       'Jaguar', 'Nissan', 'Land', 'Renault', 'Volvo', 'Force', 'Datsun',
       'Jeep', 'Isuzu', 'MG', 'Kia']


fuel=['Petrol', 'Diesel', 'LPG', 'CNG', 'Electric']

from sklearn.preprocessing import OrdinalEncoder

name_ordinal=OrdinalEncoder(categories=[name])
fuel_ordinal=OrdinalEncoder(categories=[fuel])
seller_ordinal=OrdinalEncoder(categories=[seller_type])
tran_ordinal=OrdinalEncoder(categories=[transmission])
owner_ordinal=OrdinalEncoder(categories=[owner])
company_ordinal=OrdinalEncoder(categories=[company])



df["name"]=name_ordinal.fit_transform(df[["name"]]).astype(int)
# df["company"]=company_ordinal.fit_transform(df[["company"]]).astype(int)
df["seller_type"]=seller_ordinal.fit_transform(df[["seller_type"]]).astype(int)
df["transmission"]=tran_ordinal.fit_transform(df[["transmission"]]).astype(int)
df["owner"]=owner_ordinal.fit_transform(df[["owner"]]).astype(int)
df["fuel"]=fuel_ordinal.fit_transform(df[["fuel"]]).astype(int)


x=df[['name','year','km_driven','fuel',"seller_type","transmission","owner"]]
y=df[["selling_price"]]

# print(x.head())
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)



from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=10)
rfr.fit(x_train,y_train)

y_pred_new=rfr.predict(x_test)

from sklearn.metrics import r2_score
r2_score(y_test,y_pred_new)

