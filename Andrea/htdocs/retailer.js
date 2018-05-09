var app = angular.module("sampleApp",[]);

app.controller("SampleController", function($scope){
  console.log("Controller is ready");
  /* replace mainContents by condition */
  $scope.home = function() {
    console.log("You click home!");
    this.page_home = true;
    this.page_01 = false;
    this.page_01_2 = false;
    this.page_02 = false;
    this.page_03 = false;
    this.page_04 = false;
  };
  $scope.callAboutSurvey = function() {
    console.log("You click button 1!");
    this.page_home = false;
    this.page_01 = true;
    this.page_01_2 = false;
    this.page_02 = false;
    this.page_03 = false;
    this.page_04 = false;
  };
  $scope.callAboutBGuide = function() {
    console.log("You click button 1_2!");
    this.page_home = false;
    this.page_01 = false;
    this.page_01_2 = true;
    this.page_02 = false;
    this.page_03 = false;
    this.page_04 = false;
  };  
  $scope.callCampaign = function() {
    console.log("You click button 2!");
    this.page_home = false;
    this.page_01 = false;
    this.page_01_2 = false;
    this.page_02 = true;
    this.page_03 = false;
    this.page_04 = false;
  };
  $scope.callMakeup = function() {
    console.log("You click button 3!");
    this.page_home = false;
    this.page_01 = false;
    this.page_01_2 = false;
    this.page_02 = false;
    this.page_03 = true;
    this.page_04 = false;
  };
  $scope.justArrived = function() {
    console.log("You click button 4!");
    this.page_home = false;
    this.page_01 = false;
    this.page_01_2 = false;
    this.page_02 = false;
    this.page_03 = false;
    this.page_04 = true;
  };
})