# ********************************************************************************
# If you should have any comments, suggestions or improvements to these samples, 
# we welcome you to contact us at SampleCode@melissadata.com also please visit our 
# developers bulletin board at forum.melissadata.com.
# ********************************************************************************

import mdAddrPythonWrapper

# ********************** LICENSE STRINGS ***********************
#      To unlock the full functionality of Address Object,    
#  please call a sales representative at 1-800-MELISSA ext. 3 
#          (1-800-635-4772 x3) for a license string.          
#   Address Object will function in Demo mode without a valid 
#         license and validate Nevada addresses only          
#             REPLACE "DEMO" with LICENSE STRING                    
#
#   SetLicenseString will also check for a valid license in the 
#   MDADDR_LICENSE(Environment) variable. This allows you to  
#   modify the license without recompiling the project
# **************************************************************
License = r"I2UjSzpK0xU/hM/DszyU6D==mwh5KuGH1aNqcnmPpbEJmr==qGLOEIpJJpNj/LxbSAq3oA=="

# ************************ DATA FILE PATH  ***********************
#   File location path is set to the default Data File location.  
#   Change this value if you installed the data files to a        
#   different folder.                                             
#   The Data Files Directory must contain the following files:   
#   mdAddr.dat, mdAddr.lic, mdAddr.nat, and mdAddr.str
# ****************************************************************
DataPath = r"E:\Program Files\Melissa Data\DQT\Data"


# Create Address Object
mdAddr = mdAddrPythonWrapper.mdAddr()

# Set License String
mdAddr.SetLicenseString(License)
    
# Initialize Data Files
mdAddr.SetPathToUSFiles(DataPath)

# CASS required add-ons for highest level of validation. Should be used by non-demo users.
# mdAddr.SetPathToDPVDataFiles(DataPath)
# mdAddr.SetPathToLACSLinkDataFiles(DataPath)
# mdAddr.SetPathToSuiteLinkDataFiles(DataPath)

# mdAddr.SetPathToRBDIFiles(DataPath)     #Delivery Indicator Add-on (Residence or Business)
# mdAddr.SetPathToCanadaFiles(DataPath)   #Canadian Address Validation Add-on
# mdAddr.SetPathToSuiteFinderDataFiles(DataPathLocation);  #AddressPlus Add-on (appends residential suites)

result = mdAddr.InitializeDataFiles()

if result != 0:
    print "Initialize Error: ", mdAddr.GetInitializeErrorString()
    exit()

print "===============================================\n"
print "    ADDRESS OBJECT PYTHON INTERFACE EXAMPLE\n"
print "            BuildNumber: ", mdAddr.GetBuildNumber() 
print "          Database Date: ", mdAddr.GetDatabaseDate()
print " DatabaseExpirationDate: ", mdAddr.GetExpirationDate()
print "===============================================\n"

while(1):
    Company = raw_input("  Enter Company: ")
    if (Company == '0'):
       break
    Address = raw_input("  Enter Address: ")
    Address2 = raw_input(" Enter Address2: ")
    City = raw_input("     Enter City: ")
    State = raw_input("    Enter State: ")
    Zip = raw_input("      Enter Zip: ")
    LastName = raw_input(" Enter LastName: ")
    
    # clear any remaining properties froma previous call
    mdAddr.ClearProperties()

    mdAddr.SetCompany(Company)
    mdAddr.SetAddress(Address)
    mdAddr.SetAddress2(Address2)
    mdAddr.SetCity(City)
    mdAddr.SetState(State)
    mdAddr.SetZip(Zip)
    mdAddr.SetLastName(LastName)

    mdAddr.VerifyAddress()
    print "\n============AddressObject Outputs=============\n"
    print "\n"
    print "          Company: ", mdAddr.GetCompany() 
    print "          Address: ", mdAddr.GetAddress() 
    print "         Address2: ", mdAddr.GetAddress2()
    print "            Suite: ", mdAddr.GetSuite()
    print "             City: ", mdAddr.GetCity()
    print "            State: ", mdAddr.GetState() 
    print "          ZipCode: ", mdAddr.GetZip()
    print "            Plus4: ", mdAddr.GetPlus4()
    print "\n"
    print "Results Codes... "
    ResultsString = mdAddr.GetResults()
    
    
    if (ResultsString.find("AS01")!= -1) or (ResultsString.find("AS02")!= -1) or (ResultsString.find("AS03")!= -1):
    # the address was verified       
        if (ResultsString.find("AS01")!= -1):
            print " AS01: Address Matched to Postal Database and is deliverable"
        elif (ResultsString.find("AS02")!= -1):
            print " AS02: Address matched to USPS database but a suite was missing or invalid"
        elif (ResultsString.find("AS03")!= -1):
            print " AS03: Valid physical address not serviced by the USPS"
     
    # Display additional level of verification/comments      
    if (ResultsString.find("AS09")!= -1):
        print " AS09: Foreign Postal Code Detected "
    if (ResultsString.find("AS10")!= -1):
        print " AS10: Address Matched to CMRA"
    if (ResultsString.find("AS13")!= -1):
        print " AS13: Address has been Updated by LACSLink "
    if (ResultsString.find("AS14")!= -1):
        print " AS14: Suite Appended by SuiteLink "
    if (ResultsString.find("AS15")!= -1):
        print " AS15: Suite Appended by SuiteFinder "
    if (ResultsString.find("AS16")!= -1):
        print " AS16: Address is vacant."
    if (ResultsString.find("AS17")!= -1):
        print " AS17: Alternate delivery."
    if (ResultsString.find("AS18")!= -1):
        print " AS18: DPV processing was terminated artificially created adresses detected."
    if (ResultsString.find("AS20")!= -1):
        print " AS20: Address Deliverable by USPS only "
    if (ResultsString.find("AS21")!= -1):
        print " AS21: Alternate Address Suggestion Found."
    if (ResultsString.find("AS22")!= -1):
        print " AS22: No Alternate Address Suggestion Found."
    if (ResultsString.find("AS23")!= -1):
        print " AS23: Extraneous information found "

   
   # there was an error in verifying the address
    if (ResultsString.find("AE")!= -1):
        print " The addresss could not be verified... "
    if (ResultsString.find("AE01")!= -1):
        print " AE01: Zip Code Error "
    if (ResultsString.find("AE02")!= -1):
        print " AE02: Unknown Street Error "
    if (ResultsString.find("AE03")!= -1):
        print " AE03: Component Mismatch Error "
    if (ResultsString.find("AE04")!= -1):
        print " AE04: Non-Deliverable Address Error "
    if (ResultsString.find("AE05")!= -1):
        print " AE05: Multiple Match Error "
    if (ResultsString.find("AE06")!= -1):
        print " AE06: Early Warning System Error "
    if (ResultsString.find("AE07")!= -1):
        print " AE07: Missing Minimum Address Input "
    if (ResultsString.find("AE08")!= -1):
        print " AE08: Suite Range Invalid Error"
    if (ResultsString.find("AE09")!= -1):
        print " AE09: Suite Range Missing Error "
    if (ResultsString.find("AE10")!= -1):
        print " AE10: Primary Range Invalid Error "
    if (ResultsString.find("AE11")!= -1):
        print " AE11: Primary Range Missing Error "
    if (ResultsString.find("AE12")!= -1):
        print " AE12: PO, HC, or RR Box Number Invalid "
    if (ResultsString.find("AE13")!= -1):
        print " AE13: PO, HC, or RR Box Number Missing "
    if (ResultsString.find("AE14")!= -1):
        print " AE14: CMRA Secondary Missing Error"

    # program can not attempt address lookup
    if (ResultsString.find("AE15")!= -1):
        print " AE15: Demo Mode limitation"
    if (ResultsString.find("AE16")!= -1):
        print " AE16: Expired Database, Please Update" 
        
    if (ResultsString.find("AE17")!= -1):
        print " AE17: Unnecessary Suite Error "
    if (ResultsString.find("AE19")!= -1):
        print " AE19: Max time for FindSuggestion exceeded "
    if (ResultsString.find("AE20")!= -1):
        print " AE20: FindSuggestion cannot be used"
  
    # there was a change made to the input data         
    if (ResultsString.find("AC01")!= -1):
        print " AC01: ZIP Code Change" 
    if (ResultsString.find("AC02")!= -1): 
        print " AC02: State Change" 
    if (ResultsString.find("AC03")!= -1):
        print " AC03: City Change" 
    if (ResultsString.find("AC04")!= -1):
        print " AC04: Base/Alternate Change" 
    if (ResultsString.find("AC05")!= -1):
        print " AC05: Alias Name Change" 
    if (ResultsString.find("AC06")!= -1):
        print " AC06: Address1/Address2 Swap" 
    if (ResultsString.find("AC07")!= -1):
        print " AC07: Address1/Company Swap" 
    if (ResultsString.find("AC08")!= -1):
        print " AC08: Plus4 Change" 
    if (ResultsString.find("AC09")!= -1):
        print " AC09: Urbanization Change" 
    if (ResultsString.find("AC10")!= -1):
        print " AC10: Street Name Change" 
    if (ResultsString.find("AC11")!= -1):
        print " AC11: Street Suffix Change"
    if (ResultsString.find("AC12")!= -1):
        print " AC12: Street Directional Change" 
    if (ResultsString.find("AC13")!= -1):
        print " AC13: Suite Name Change"        
    
    print "\n"
    print "            Carrier Route: ", mdAddr.GetCarrierRoute()
    print "      Delivery Point Code: ", mdAddr.GetDeliveryPointCode()
    print "  DeliveryPointCheckDigit: ", mdAddr.GetDeliveryPointCheckDigit()
    print "            DPV Footnotes: ", mdAddr.GetDPVFootnotes()
    print "\n"
    print "        Address Type Code: ", mdAddr.GetAddressTypeCode()
    print "      Address Type String: ", mdAddr.GetAddressTypeString()
    print "        City Abbreviation: ", mdAddr.GetCityAbbreviation()
    print "              County Name: ", mdAddr.GetCountyName()
    print "              County Fips: ", mdAddr.GetCountyFips()
    print "             Country Code: ", mdAddr.GetCountryCode()
    print "   Congressional District: ", mdAddr.GetCongressionalDistrict()
    print "                Time Zone: ", mdAddr.GetTimeZone()
    print "           Time Zone Code: ", mdAddr.GetTimeZoneCode()
    print "             Urbanization: ", mdAddr.GetUrbanization()
    print "                 Zip Type: ", mdAddr.GetZipType()
    print "\n"
    print "     Parsed Address Range: ", mdAddr.GetParsedAddressRange()
    print "     Parsed Pre Direction: ", mdAddr.GetParsedPreDirection() 
    print "       Parsed Street Name: ", mdAddr.GetParsedStreetName()
    print "            Parsed Suffix: ", mdAddr.GetParsedSuffix()
    print "    Parsed Post Direction: ", mdAddr.GetParsedPostDirection() 
    print "        Parsed Suite Name: ", mdAddr.GetParsedSuiteName()
    print "       Parsed Suite Range: ", mdAddr.GetParsedSuiteRange()
    print " ParsedPrivateMailboxName: ", mdAddr.GetParsedPrivateMailboxName()
    print "  ParsedPrivMailboxNumber: ", mdAddr.GetParsedPrivateMailboxNumber()
    print "           Parsed Garbage: ", mdAddr.GetParsedGarbage()
    print "\n" 
    print "                      MSA: ", mdAddr.GetMsa()
    print "                     PMSA: ", mdAddr.GetPmsa()
    print "                     CMRA: ", mdAddr.GetCMRA()
    print "          Private Mailbox: ", mdAddr.GetPrivateMailbox() 
    print "\n"
    print "               ELot Order: ", mdAddr.GetELotOrder()
    print "              ELot Number: ", mdAddr.GetELotNumber()
    print "                     LACS: ", mdAddr.GetLACS()  
    print "        LACSLinkIndicator: ", mdAddr.GetLACSLinkIndicator()  
    print "       LACSLinkReturnCode: ", mdAddr.GetLACSLinkReturnCode()
    print "   Suite Link Return Code: ", mdAddr.GetSuiteLinkReturnCode()  
    print "                      EWS: ", mdAddr.GetEWSFlag()
    print "                     RBDI: ", mdAddr.GetRBDI() 
    
    
    print "\n"
    print "To quit program, input Company: '0' \n"
userinput = raw_input("Goodbye, Press <Enter> to quit... ")
