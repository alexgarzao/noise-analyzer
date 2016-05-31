Feature: Test with recorded data in CVS files
  In order to test analyzer class
  We'll use some recorded data stored in CSV files

  Scenario: Testing with the original sample
    Given I have the file "230V_50Hz_ADCdiv1.csv"
    When I send this file to analyzer
    Then I see noise values in file "../noise_connection__1.csv" equals to file "230V_50Hz_ADCdiv1.noise.csv"

  Scenario: Testing again with the original sample
    Given I have the file "230V_50Hz_ADCdiv1.csv"
    When I send this file to analyzer
    Then I see noise values in file "../noise_connection__2.csv" equals to file "230V_50Hz_ADCdiv1.noise.csv"
