Feature: Test with recorded data in CVS files
  In order to test analyzer class
  We'll use some recorded data stored in CSV files

  Scenario: Testing with original sample
    Given I have the file "230V_50Hz_ADCdiv1"
    When I send this file to analyzer
    Then I see noise values equals to file "230V_50Hz_ADCdiv1.noise"
