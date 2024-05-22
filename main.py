import snowflake.connector

from config import connect_to_snowflake

def create_table(conn):
    with conn.cursor() as cursor:
       cursor.execute("""
            CREATE TABLE IF NOT EXISTS LINEITEMS (
transaction_id INT, store_id VARCHAR, tender_id VARCHAR, tender_name VARCHAR, tender_type VARCHAR, tender_amount FLOAT, change_indicator VARCHAR, operator_id VARCHAR, line_number INT, date_processed TIMESTAMP_NTZ, variabledata VARIANT
)
    
        """)
conn = connect_to_snowflake()
cur = conn.cursor()
create_table(conn)

import pandas as pd

# Load the CSV file
file_path = 'C:/Locations.csv'
data = pd.read_csv(file_path)

for index, row in data.iterrows():
    insert_statement = f"""
    INSERT INTO CUSTOMER_ONBOARDING.CUSTOMER_ONBOARDING.LOCATIONS (
        ORGANIZATIONKEY,
        LOCATION_ID,
        LOCATION_DESC,
        LAST_TANK_READING_DATE,
        FIRST_TRANSACTION_DATE,
        LAST_REMODEL_DATE,
        CLOSING_DATE,
        GPS_LATITUDE,
        GPS_LONGITUDE,
        GPS_ADDRESS1,
        GPS_ADDRESS2,
        GPS_CITY,
        GPS_STATE,
        GPS_ZIP,
        CORPSITE,
        BUSINESS_ENTITY_DESC,
        BUSINESS_ENTITY_ID,
        PAPERWORK_SET_DEPLOYMENT_DESC,
        PAPERWORK_SET_DEPLOYMENT_ID,
        DESKTOP_DEPLOYMENT_DESC,
        DESKTOP_DEPLOYMENT_ID,
        FUEL_BRAND_DESC,
        FUEL_BRAND_ID,
        ALL_BRANDED_FOOD_DESC,
        ALL_BRANDED_FOOD_ID,
        CORPORATE_DESC,
        CORPORATE_ID,
        DIRECTOR_DESC,
        DIRECTOR_ID,
        COORDINATOR_DESC,
        COORDINATOR_ID,
        SUPERVISOR_DESC,
        SUPERVISOR_ID,
        SITE_DESC,
        SITE_ID,
        DELI_LOCATIONS_DESC,
        DELI_LOCATIONS_ID,
        STORES_BY_COUNTY_DESC,
        STORES_BY_COUNTY_ID,
        BUDGET_PAYROLL_HOURS_DESC,
        BUDGET_PAYROLL_HOURS_ID,
        PB_RETAIL_LOCATIONS_DESC,
        PB_RETAIL_LOCATIONS_ID,
        PB_CIGARETTES_DESC,
        PB_CIGARETTES_ID,
        PB_SLEDD_DESC,
        PB_SLEDD_ID,
        PB_BEER_DESC,
        PB_BEER_ID,
        PB_TOBACCO_DESC,
        PB_TOBACCO_ID,
        PB_STATE_DESC,
        PB_STATE_ID,
        PB_BEVERAGE_DESC,
        PB_BEVERAGE_ID,
        PB_CAR_WASH_DESC,
        PB_CAR_WASH_ID,
        STATE_DESC,
        STATE_ID,
        STORE_TYPE_DESC,
        STORE_TYPE_ID,
        FUEL_SUPPLIER_DESC,
        FUEL_SUPPLIER_ID,
        PB_COMMANDER_DESC,
        PB_COMMANDER_ID,
        PB_FRITO_LAY_DESC,
        PB_FRITO_LAY_ID,
        PB_ITG_REBATES_DESC,
        PB_ITG_REBATES_ID,
        PB_FOUNTAIN_DESC,
        PB_FOUNTAIN_ID,
        TIME_ZONE_ID,
        SITE_ID_FORMATTED,
        SUBWAY_ARBYS_DESC,
        SUBWAY_ARBYS_ID
    ) VALUES (
        '{row['organizationkey']}',
        '{row['LocationID']}',
        '{row['LocationDesc']}',
        '{row['LastTankReadingDate']}',
        '{row['FirstTransactionDate']}',
        '{row['LastRemodelDate']}',
        '{row['ClosingDate']}',
        {row['GPSLatitude'] if pd.notna(row['GPSLatitude']) else 'NULL'},
        {row['GPSLongitude'] if pd.notna(row['GPSLongitude']) else 'NULL'},
        '{row['GPSAddress1']}',
        '{row['GPSAddress2']}',
        '{row['GPSCity']}',
        '{row['GPSState']}',
        '{row['GPSZip']}',
        '{row['Corpsite']}',
        '{row['BusinessEntitydesc']}',
        '{row['BusinessEntityid']}',
        '{row['PaperworkSetDeploymentdesc']}',
        '{row['PaperworkSetDeploymentid']}',
        '{row['DesktopDeploymentdesc']}',
        '{row['DesktopDeploymentid']}',
        '{row['FuelBranddesc']}',
        '{row['FuelBrandid']}',
        '{row['AllBrandedFooddesc']}',
        '{row['AllBrandedFoodid']}',
        '{row['Corporatedesc']}',
        '{row['Corporateid']}',
        '{row['Directordesc']}',
        '{row['Directorid']}',
        '{row['Coordinatordesc']}',
        '{row['Coordinatorid']}',
        '{row['Supervisordesc']}',
        '{row['Supervisorid']}',
        '{row['Sitedesc']}',
        '{row['Siteid']}',
        '{row['DeliLocationsdesc']}',
        '{row['DeliLocationsid']}',
        '{row['StoresbyCountydesc']}',
        '{row['StoresbyCountyid']}',
        '{row['BudgetPayrollHoursdesc']}',
        '{row['BudgetPayrollHoursid']}',
        '{row['PBRetailLocationsdesc']}',
        '{row['PBRetailLocationsid']}',
        '{row['PBCigarettesdesc']}',
        '{row['PBCigarettesid']}',
        '{row['PBSledddesc']}',
        '{row['PBSleddid']}',
        '{row['PBBeerdesc']}',
        '{row['PBBeerid']}',
        '{row['PBTobaccodesc']}',
        '{row['PBTobaccoid']}',
        '{row['PBStatedesc']}',
        '{row['PBStateid']}',
        '{row['PBBeveragedesc']}',
        '{row['PBBeverageid']}',
        '{row['PBCarWashdesc']}',
        '{row['PBCarWashid']}',
        '{row['Statedesc']}',
        '{row['Stateid']}',
        '{row['Storetypedesc']}',
        '{row['Storetypeid']}',
        '{row['FuelSupplierdesc']}',
        '{row['FuelSupplierid']}',
        '{row['PBCommanderdesc']}',
        '{row['PBCommanderid']}',
        '{row['PBFritoLaydesc']}',
        '{row['PBFritoLayid']}',
        '{row['PBITGRebatesdesc']}',
        '{row['PBITGRebatesid']}',
        '{row['PBFountaindesc']}',
        '{row['PBFountainid']}',
        '{row['TimeZoneID']}',
        '{row['SiteIDFormatted']}',
        '{row['SubwayArbysdesc']}',
        '{row['SubwayArbysid']}'
    );
    """
    cur.execute(insert_statement)

# Close the connection
cur.close()
conn.close()