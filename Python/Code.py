print('Welcome to Forest Survey of India')
try:
    import urllib.request
    from PIL import Image
    urllib.request.urlretrieve('https://fsi.nic.in/img/resources/logo.png','logo.png')
    sr = Image.open('logo.png')
    sr.show()
except urllib.error.URLError:
    print('"Check your network connection, unable to display the logo."')
while True:
    pr=input('\nImportant Links:\n1. About Us\n2. Zonal Offices\n3. Forest Fire\n4. Reports\n5. Projects\n6. Contact Us\n\nEnter the S.No. of the link\n')
    if pr=='1':
        while True:
            ar=input('\n1. Brief History\n2. Objectives\n3. Major Activities\n4. Organisation Setup\n\nEnter the S.No. of the Link\n')
            if ar=='1':
                print('\nForest Survey of India (FSI), is a premier national organization under the union Ministry of Environment and Forests, responsible for assessment and monitoring of the forest resources of the country regularly. In addition, it is also engaged in providing the services of training, research and extension. Established on 1 June 1981, the Forest Survey of India succeeded the "Preinvestment Survey of Forest Resources" (PISFR), a project initiated in 1965 by Government of India with the sponsorship of FAO and UNDP.\n\nThe main objective of PISFR was to ascertain the availability of raw material for establishment of wood based industries in selected areas of the country. In its report in 1976, the National Commission on Agriculture (NCA) recommended for the creation of a National Forest Survey Organization for a regular, periodic and comprehensive forest resources survey of the country leading to creation of FSI. After a critical review of activities undertaken by FSI, Government of India redefined the mandate of FSI in 1986 in order to make it more relevant to the rapidly changing needs and aspirations of the country.')
                break
            elif ar=='2':
                print("\n1. To prepare State of Forest Report biennially, providing assessment of latest forest cover in the country and monitoring changes in these.\n2. To conduct inventory in forest and non-forest areas and develop database on forest tree resources.\n3. To prepare thematic maps on 1:50,000 scale, using aerial photographs.\n4. To function as a nodal agency for collection, compilation, storage and dissemination of spatial database on forest resources.\n5. To conduct training of forestry personnel in application of technologies related to resources survey, remote sensing, GIS, etc.\n6. To strengthen research & development infrastructure in FSI and to conduct research on applied forest survey techniques.\n7. To support State/UT Forest Departments (SFD) in forest resources survey, mapping and inventory.\n8. To undertake forestry related special studies/consultancies and custom made training courses for SFD's and other organisations on project basis.")
                break
            elif ar=='3':
                print('\n1. Forest Cover Assessment\n2. Inventory of Forest areas\n3. Inventory of Trees Outside Forests (Rural & Urban)\n4. Inventory data processing\n5. Methodology Design\nTraining and Extension\n6. Projects and Consultancies')
                break
            elif ar=='4':
                print('\nFSI is headed by a Director General supported by two Joint Directors and eight Deputy Directors at headquarters. Each Zonal office is headed by a Regional Director and supported by one or two Deputy Directors. The Joint Directors at the headquarters head two units namely Forest Geoinformatics Division (FGD) and Forest Inventory & Training Division (FITD). FGD conducts assessment of forest cover, thematic mapping, production of maps, etc. FITD unit is concerned with inventory of tree resources inside and outside the forests, conducting of training courses, extension works, publication of reports, maintenance of library, etc. The total sanctioned strength of the organisation is 436, which includes members of the Indian Forest Service and Indian Statistical Service on deputation. The Organisational table of FSI is shown below:\n')
                from tabulate import tabulate
                print(tabulate([['FGD','Forest Geoinformatics Division'],['FITD','Forest Inventory & Training Division'],['FCM','Forest Cover Mapping'],['FI','Forest Inventory'],['TRG','Training'],['SM','Systems Manager'],['EXTN','Extension'],['P&AD','Personnel & Administration Division']],tablefmt='grid'))
                break
            else:
                ar+='1'
    elif pr=='2':
        while True:
            ar=input('\nEach Zonal office is headed by a Regional Director supported by Deputy Directors and secretarial and field staff. Its main function is field data collection for forest inventory, though their functions have expanded to include forest cover mapping of selected states. There are four zonal offices of FSI given below:\n\n1. Northern Zone Shimla\n2. Eastern Zone Kolkata\n3. Central Zone Nagpur\n4. Southern Zone Banglore\n\nEnter the S.No. of the Zonal Office to know the basic detail of it:\n')
            if ar=='1':
                print('The Northern Zone office of FSI is in Shimla with jurisdiction over the States of Jammu and Kashmir, Himachal Pradesh, Uttar Pradesh, Haryana, Punjab, Chandigarh, Rajasthan, Delhi and Uttaranchal. Its mandatory works are:\n\nCarries out forest cover assessment beyond its domain, including a study on household wood consumption in rural Meghalaya (1986-88), preparation of a survey scheme and a field work of survey operation in 1979 in Western Nepal.')
                break
            elif ar=='2':
                print('The Eastern Zone office of PISFR was created in the year 1974. After the reorganization of PISFR (1981), the office has been functioning as the Eastern Zone office of FSI. Its mandatory works are:\n\nEngaged in inventory of forests and TOF in its area of jurisdiction including Bihar (including present Jharkhand), West Bengal, Odisha, Sikkim, Meghalaya, Tripura, Manipur, Nagaland, Mizoram, Assam, Arunachal Pradesh and the Union Territory of Andaman and Nicobar Islands. Also collaborated with the Nagaland Forest Department in an inventory project in the State.')
                break
            elif ar=='3':
                print('The Central Zone office of PISFR was set up at Jagdalpur in 1966 later shifted to Nagpur in 1976.Area under its jurisdiction include the states of Madhya Pradesh (MP), Maharashtra, Chhattisgarh, Gujarat, Goa, Dadra & Nagar Haveli (UT), and Daman & Diu (UT). Apart from conducting inventory of forests and Trees outside Forests (TOF), it also carries out:\n\nForest Cover Assessment of Maharashtra, MP, Chhattisgarh, Gujarat and Goa.\nExtensive training programs for State Forest Departments (SFDs) in Application of Remote Sensing, GIS & GPS in forestry, Inventory techniques, e-Green Watch and Decision Support System (DSS).')
                break
            elif ar=='4':
                print('The Southern Zone office was established during 1982. Its mandate is to conduct inventory of Forests and TOF in the states of Karnataka, Andhra Pradesh, Kerala, Tamil Nadu (TN) and Telangana. Special studies on Mangroves & TOF inventory in TN has also been carried out by the zone.')
                break
            else:
                ar+='1'
    elif pr=='3':
        import webbrowser
        ar = 'Forest Fire Studies.pdf'
        webbrowser.open_new(ar)
    elif pr=='4':
        while True:
            ar=input('\n1. Carbon Report\n2. Vulnerability of Forest Fire\n\nEnter the S.No. of the report\n')
            if ar=='1':
                import webbrowser
                th='Carbon Report.pdf'
                webbrowser.open_new(th)
                break
            elif ar=='2':
                import webbrowser
                th='Vulnerability of Forest Fire.pdf'
                webbrowser.open_new(th)
                break
            else:
                ar+='1'
    elif pr=='5':
        while True:
            ar=input('\n1. Completed Projects\n2. Ongoing Projects\n\nEnter the S.No. of the Link\n')
            if ar=='1':
                while True:
                    th=input('\nCompleted projects are as follows:\n\n1. Application of GIS in Watershed Management\n2. Forest Cover in Tiger Reserves\n3. Geo-spatial Database for Corbett National Park\n4. National Afforestation Programme (NAP)\n5. Pilot study: Assessment of Status of Sustainability of Forest Resources\n\nEnter the S.No. of the completed project\n')
                    if th=='1':
                        print('\nProject Area: Uttari Koshi, is situated in Almora district and extends over 454.32 km^2. It has 15 micro water-sheds and forms a part of watershed of Kosi river. There are 4 development blocks of in the project area covering 341 villages. The altitude varies between 1000 m to 2750 m above mean sea level.\n\nMethodology:\n1. Data acquisition\n2. Data input for creation of Data base\n3. Data interpretation and analysis\n4. Outputs (Landuse Maps)')
                        break
                    elif th=='2':
                        print('\nObjectives:\n1. To prepare a comprehensive report on the status of forest cover in 28 Tiger Reserves of India using the technique of digital interpretation of satellite data.\n2. To generate the maps showing the status of forest cover for each Tiger Reserve for the period 1997 and 2002 and change of forest cover during the period 1997-2002. In these maps the minimum area of delineation would be one hectare.\n\nStudy Area: The peripheral area of the 10 km radial distance from the periphery of Tiger Reserve boundary (referred to as ‘Outer Surround’) was also studied in addition to the total area inside the 28 TRs. The states of vegetation cover was also assessed and mapped for the year 2000 with the help of digital satellite data acquired from National Remote Sensing Agency (NRSA)\n\nMethodology: The assessment of forest cover involved digital image processing (DIP) followed by intensive field verification. The hard copy maps were scanned, geo-referenced with Survey of India toposheets and were digitized in the vector format and additional boundary of the Outer Surround was also created. During the period 1997-2002 the overall forest cover in all the Tiger Reserves is estimated to decrease by 1994 km2. Out of the total decrease 62 km2 is estimated to have decreased during 1997-2000 and 32 km2 during 2000-2002. The VDF increased by 33 km2, the OF increased by 124 km2 , whereas the MDF decreased by 251 km2. Five Tiger Reserves showed an increase in forest cover, eleven TRs showed a decrease, and 12 TRs showed no change. Overall there was a decrease of 124 km2 of forest cover. Of this, 74 km2 decreased between 1997-2000 and 50 km2 between 2000-2002. The overall loss in forest cover in the Outer Surrounds exceeded that within TRs. The satellite data specifications were as under:\n')
                        from tabulate import tabulate
                        print(tabulate([['Satellite','IRS-IC/1D'],['Sensor','LISS-III'],['Data Period','1997, 2000 & 2002'],['Product','Digital Data'],['Spatial Resolution','23.5 m x 23.5 m'],['Spectral Resolution','4 bands']],tablefmt='grid'))
                        break
                    elif th=='3':
                        print('\nStudy Area: Corbett Tiger Reserve (CTR), the first Tiger Reserve to be established in the country in 1973 under ‘Project Tiger’. This park represents the amalgamation of culture of these hill regions, and displays amazing landscapes and diverse flora and fauna. The park receives about 1500 mm to 1600 mm of rainfall mainly during the monsoon though some winter rain always occurs. The temperature ranges between 4°C in winter to 42°C during the summer season. The hydro-electric power plant located at the Kalagarh dam supplies electricity within the park. The park is the habitat for numerous animal, bird and tree species, like Black Bears, Tigers, Leopards, deer, Asian elephants, crocodiles and other aquatic species.\n\nData Input: DI includes (i)Thematic Map of Corbett National Park on 1:25,000 based on interpretation of aerial photographs (ii) Forest Cover map on 1:50,000 scale based on satellite data of year 2000 (iii) SOI toposheets on 1:50,000 scale covering the area (iv) IRS 1D LISS III data of March 2001 for digital classification of Forest Types. and (v) Databases provided by the authorities of the Corbett Tiger Reserve.\n\nOutputs: The total area is estimated by the CTR is 1288.32 km2. There are about 58 forest chaukis, 22 rest houses and 12 Range offices within CTR. The perspective view of CTR with the false colour composite of the satellite imagery draped over the digital elevation model, which helps in the visual understanding of the geomorphology of the area. Ground verification was carried out in the southern, eastern and central parts of the CTR. Three density classes namely, very dense (canopy density of more than 70%), moderately dense (canopy density of 40% to 70%) and open (canopy density of 10% to 40%) forests, along with scrub (canopy density of less than 10%, in and around forest areas), water bodies and non-forest areas were classified. Area covered by each forest is given below:\n')
                        import sqlite3
                        an=sqlite3.connect('projectfsi.db')
                        a=an.cursor()
                        a.execute('CREATE TABLE IF NOT EXISTS cnp(Forest_type VARCHAR,Area_in_sq_km FLOAT,Percentage_of_total_area FLOAT)')
                        a.execute('select count(*)from cnp')
                        sr=a.fetchone()[0]
                        print('Below given data is (Forest type,Area in sq.km,% of total area):\n')
                        if sr==0:
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Pure Sal',540.71,41.97)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Mixed Sal',207.2,16.08)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Miscellaneous',222.75,17.29)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Grass/Riverbed',109.12,8.47)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Scrub',74.09,5.75)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Plantation',89.87,6.98)")
                            a.execute("insert into cnp(Forest_type,Area_in_sq_km,Percentage_of_total_area)values('Water',44.59,3.46)")
                            an.commit()
                        a.execute('select * from cnp')
                        ir=a.fetchall()
                        for am in ir:
                            print(am)
                        an.close()
                        break
                    elif th=='4':
                        print('\nThe main objectives of the project are as follows:\n• Monitoring of area coverage and estimate at the National Level the area coverage of selected FDAs.\n• To estimate at the national level survival percentage of plantations (species wise) raised by FDAs in forest and outside forests areas.\n• To assess growth parameters of trees planted under NAP scheme.\n\nMethodology: The study area for this survey is considered as FDA areas of the Districts. FDAs are selected randomly distributed over the whole country. The patches of FDAs are further stratified into five strata i.e. four strata in Forest Area(FA) based on patch area, and one stratum in non-forest area (NFA), which are the sampling units. The selected patches within a FDA are physically verified with the help of GPS by traversing the whole boundary. The expected results of the survey would be with 15% permissible error at 95% probability level at National level.\n\nThe following data are collected from the selected FDAs:\n(i) Area of patches\n(ii) Total number of plants planted in the plot\n(iii) Total number of plants survived in the plot\n(iv) Name of tree species, height and number of diseased/dead plants in the plot.')
                        break
                    elif th=='5':
                        print('\nThe aim of the pilot study was to develop a methodology for assessment of sustainability of forest resources in the country and to actually make the first rough assessment in the process. This was accomplished by carrying out the following tasks for each criterion:\n• Identification of variables relevant to each criterion.\n• Compilation of data and trends for different variables identified for each criterion.\n• Making qualitative assessment of sustainability of forest resources in India.\n\nThe pilot study for India was carried out in five stages over two expert consultations. A group of 33 experts representing a number of stakeholders in forest management was invited to participate in the pilot study. Foresters, conservationists, academicians and biologists representing Government departments and institutions (both central and state) formed this group but forest industry, non-government organizations and sections of people living near or in the forest were prominent groups missing from the exercise.\n\nStage I: Identification of variables\nStage II: Assigning of weights to each criterion and variable\nStage III: Compilation of national data and trends\nStage IV: Evaluation of data and trends\nStage V: Assessment of sustainability of forest resources\n\nA report on Pilot Study on Assessment of status of sustainability of forest resources in India has been published by Forest Survey of India describing the details about different criterion required for sustainability. Status of Sustainability of Forest Resources of India through Criteria is given below:\n')
                        try:
                            import mysql.connector
                            an=mysql.connector.connect(host='localhost',user='Sriram P G',passwd='prarsri',database='projectfsi')
                            a='select * from ps'
                            sr=an.cursor()
                            sr.execute(a)
                            ir=sr.fetchall()
                            for am in ir:
                              print('S_No: ',am[0],'\nCriteria: ',am[1],'\nRelative Weight: ',am[2],'\nScore: ',am[3],'\nWeighted Score: ',am[4],'\n')
                        except mysql.connector.errors.ProgrammingError:
                            print('"Check your MySQL connection, unable to display the data."\n')
                        print('Total of Relative Weight: 100\nTotal of  Weighted Score: 55.8\n\nAnalysing the figures in the above table we find that experts are of the opinion that of all the criteria, Criterion 1(a) “Extent of Forest” and Criterion 2 “Forest Health and Vitality” are relatively more important than others.')
                    break
                break
            elif ar=='2':
                while True:
                    th=input('\nCompleted projects are as follows:\n\n1. Near Real Time Monitoring of Active Fires Using MODIS Based Web Fire Mapper\n\nEnter the S.No. of the ongoing project\n')
                    if th=='1':
                        print('\nThe methodology involves following steps:\n\n1. Acquisition of Data from the website (maps.geog.umd.edu)\n2.Processing of the point Data\n3. Geometric correction\n4. Joining of Attributes\n5. Dissemination of information')
                        break
                    else:
                        th+='1'
                break
            else:
                ar+='1'
    elif pr=='6':
        from PIL import Image
        ar= Image.open(r"D:\Project FSI\Contact.png")
        ar.show()
    else:
        pr+='1'
