package unexpectednessevaluationtool;

import java.util.ArrayList;
import java.util.HashMap;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author labpi
 */
public class ParametersEvaluation {
    
    private static int numberOfMetrics = 5;
    
    /*
    Attributes regarding the parameters
    */
    private String consumptionHistory;
    private String itemsFeatures;
    private String outputFolder;
    private HashMap<String,String> recommendationLists;
    private HashMap<String,Integer> topNRecommendationLists;
    private HashMap<Integer,String> recommendationID;
    private String ppm;
    
    private ArrayList<Boolean> metrics;
    
    private boolean statisticalSummarization;
    private boolean mean;
    private boolean median;
    private boolean sd;
    private boolean rankcurve;
    
    private boolean statisticalAnalysis;
    private boolean itemPopularity;
    private boolean historySize;
    private boolean userBias;
    private float   binSize;
    
    private boolean similarityAnalysis;
    private boolean kendall;
    private boolean pearson;
    private boolean spearman;
    
    private boolean combinationAnalysis;
    private boolean svd;
    private boolean pca;
    private boolean kpca;
    private String kpcaKernelFunction;
    
    public ParametersEvaluation(){
        this.consumptionHistory = "";
        this.itemsFeatures = "";
        this.recommendationLists = new HashMap<String,String>();
        this.topNRecommendationLists = new HashMap<String, Integer>();
        this.recommendationID = new HashMap<Integer, String>();
        this.metrics = new ArrayList<Boolean>();
        for (int i=0;i<numberOfMetrics;i++){
            this.metrics.add(Boolean.FALSE);
        }
        this.outputFolder="";
        this.ppm = "";
        
        //disabling statistical summarization
        this.statisticalSummarization = false;
        this.mean = false;
        this.median = false;
        this.sd = false;
        this.rankcurve = false;
        
        //disabling statistical analysis
        this.statisticalAnalysis = false;
        this.itemPopularity = false;
        this.historySize = false;
        this.userBias = false;
        this.binSize = 0;
        
        //disabling similarity
        this.similarityAnalysis = false;
        this.kendall = false;
        this.spearman = false;
        this.pearson = false;
        
        this.combinationAnalysis = false;
        this.svd = false;
        this.pca = false;
        this.kpca = false;
        this.kpcaKernelFunction = "rbfdot";
    }
    
    /*
    Set the consumption History
    */
    public void setConsumptionHistoryFile(String fullName){
        this.consumptionHistory = fullName;
    }
    
    /*
    Get the consumption history
    */
    public String getConsumptionHistory(){
        return this.consumptionHistory;
    }
    
    /*
    Set the Items Features
    */
    public void setItemsFeatures(String fullName){
        this.itemsFeatures = fullName;
    }
    
    
    /*
    Get the consumption history
    */
    public String getItemsFeatures(){
        return this.itemsFeatures;
    }
    
    /*
    Set the output folder
    */
    public void setOutputFolder(String outputFolder){
        this.outputFolder = outputFolder;
    }
    
    /*
    Get the output folder;
    */
    public String getOutputFolder(){
        return this.outputFolder;
    }
    
    /*
    Add a new Recommendation List. Return a integer with the result of the error
    */
    public int addRecommendationList(String fullName,String outputname, int topN, int id){
        
        //checking whether I'm attempting to add the ppm which is already there
        if (this.ppm.equals(fullName)){
            return 1;
        }
        
        //checking whether I'm attempting to submit the same file twice
        for (String r: this.recommendationLists.keySet()){
            if (r.equals(fullName)){
                return 2;
            }
        }
        
        this.recommendationLists.put(fullName, outputname);
        this.topNRecommendationLists.put(fullName, topN);
        this.recommendationID.put(id, fullName);
        return 0;
    }
    
    public void removeRecommendationList(int id){
        String fullName = this.recommendationID.get(id);
        this.recommendationLists.remove(fullName);
        this.topNRecommendationLists.remove(fullName);
        this.recommendationID.remove(id);
    }
    
    public void changeNameGivenID(int id, String outputname){
        String fullName = this.recommendationID.get(id);
        this.recommendationLists.remove(fullName);
        this.recommendationLists.put(fullName, outputname);
        int topn = this.topNRecommendationLists.get(fullName);
         this.topNRecommendationLists.remove(fullName);
        this.topNRecommendationLists.put(fullName, topn);
    }

    /*
    Getting the recommendation lists
    */
    public HashMap<String,String> getListRecommendationLists() {
        return recommendationLists;
    }
    
    /*
    Getting the recommendation lists
    */
    public String getRecommendationListName(String key){
        return this.recommendationLists.get(key);
    }
    
    public Integer getRecommendationListTopN(String key){
        return this.topNRecommendationLists.get(key);
    }
    
    /*
    Set the PPM file
    */
    public boolean setPPM(String ppmPath){
        
        for(String s: this.recommendationLists.keySet()){
            if (s.equals(ppmPath)){
                return false;
            }
        }
        this.ppm = ppmPath;
        return true;
    }
    
    public String getPPM(){
        return this.ppm;
    }
    
    /*
    Set the metric i-1 as true
    */
    public void setMetric(int index){
        this.metrics.set(index, Boolean.TRUE);
    }
    
    /*
    Unset the metric i-1 as false.
    */
    public void unsetMetric(int index){
        this.metrics.set(index, Boolean.FALSE);
    }

    /*
    Get the metrics
    */
    public ArrayList<Boolean> getMetrics() {
        return metrics;
    }
    
    /*
    Get a String of the metrics id selected.
    */
    public String getStringOfMetrics() {
        String metricsString = "";
        for (int i=0; i<metrics.size(); i++){
            if (metrics.get(i)==Boolean.TRUE){
                metricsString += String.valueOf(i+1)+" ";
            }
        }
        return metricsString.substring(0, metricsString.length() -1);
    }

    /*
    Set the Statistical Summarization
    */
    public void setStatisticalSummarization(boolean statisticalSummarization) {
        this.statisticalSummarization = statisticalSummarization;
    }
    
    

    /*
    Set the Statistical Analysis
    */
    public void setStatisticalAnalysis(boolean statisticalAnalysis) {
        this.statisticalAnalysis = statisticalAnalysis;
    }

    /*
    Set the Similarity Analysis
    */
    public void setSimilarityAnalysis(boolean similarityAnalysis) {
        this.similarityAnalysis = similarityAnalysis;
    }

    /*
    Set the Combination Analysis
    */
    public void setCombinationAnalysis(boolean combinationAnalysis) {
        this.combinationAnalysis = combinationAnalysis;
    }

    /*
    Set the Mean Analysis
    */
    public void setMean(boolean mean) {
        this.mean = mean;
    }

    /*
    Set the Meadian Analysis-
    */
    public void setMedian(boolean median) {
        this.median = median;
    }

    /*
    Set the Standard Deviation Analysis
    */
    public void setSd(boolean sd) {
        this.sd = sd;
    }

    /*
    Set the Rank Curve Analysis
    */
    public void setRankcurve(boolean rankcurve) {
        this.rankcurve = rankcurve;
    }

    /*
    Set the item popularity Analysis
    */
    public void setItemPopularity(boolean itemPopularity) {
        this.itemPopularity = itemPopularity;
    }

    /*
    Set the History Size Analysis
    */
    public void setHistorySize(boolean historySize) {
        this.historySize = historySize;
    }

    /*
    Set the user bias analysis.
    */
    public void setUserBias(boolean userBias) {
        this.userBias = userBias;
    }

    /*
    Set the binSize
    */
    public void setBinSize(float binSize) {
        this.binSize = binSize;
    }
   
    /*
    Set the kendall similarity to true of false
    */
    public void setKendall(boolean kendall){
        this.kendall = kendall;
    }
    
    /*
    Set the kendall similarity to true of false
    */
    public void setPearson(boolean pearson){
        this.pearson = pearson;
    }

    /*
    Set the kendall similarity to true of false
    */
    public void setSpearman(boolean spearman){
        this.spearman = spearman;
    }


    /*
    Set the svd Analysis
    */
    public void setSvd(boolean svd) {
        this.svd = svd;
    }

    /*
    Set PCA analysis
    */
    public void setPca(boolean pca) {
        this.pca = pca;
    }

    /*
    Set KPCA
    */
    public void setKpca(boolean kpca) {
        this.kpca = kpca;
    }

    /*
    Set the KPCA Kernel Function
    */
    public void setKpcaKernelFunction(String kpcaKernelFunction) {
        this.kpcaKernelFunction = kpcaKernelFunction;
    }

    public int getStatisticalSummarization() {
        if (this.statisticalSummarization == true){
            return 1;
        }
        return 0;
    }

    public int getMean() {
        if (this.mean == true){
            return 1;
        }
        return 0;
    }

    public int getMedian() {
        if (this.median == true){
            return 1;
        }
        return 0;
    }

    public int getSd() {
        if (this.sd == true){
            return 1;
        }
        return 0;
    }

    public int getRankcurve() {
        if (this.rankcurve == true){
            return 1;
        }
        return 0;
    }

    public int getStatisticalAnalysis() {
        if (this.statisticalAnalysis == true){
            return 1;
        }
        return 0;
    }

    public float getBinSize() {
        return binSize;
    }

    public int getItemPopularity() {
        if (this.itemPopularity == true){
            return 1;
        }
        return 0;
    }

    public int getHistorySize() {
        if (this.historySize == true){
            return 1;
        }
        return 0;
    }

    public int getUserBias() {
        if (this.userBias == true){
            return 1;
        }
        return 0;
    }

    public int getSimilarityAnalysis() {
        if (this.similarityAnalysis == true){
            return 1;
        }
        return 0;
    }

    /*
    get if kendall is set or not.
    */
    public int getKendall() {
        if (this.kendall==true){
            return 1;
        }
        return 0;
    }
    
    /*
    get if kendall is set or not.
    */
    public int getPearson() {
        if (this.pearson==true){
            return 1;
        }
        return 0;
    }
    
    /*
    get if kendall is set or not.
    */
    public int getSpearman() {
        if (this.spearman==true){
            return 1;
        }
        return 0;
    }

    public int getCombinationAnalysis() {
        if (this.combinationAnalysis == true){
            return 1;
        }
        return 0;
    }

    public int getSvd() {
        if (this.svd == true){
            return 1;
        }
        return 0;
    }

    public int getPca() {
        if (this.pca == true){
            return 1;
        }
        return 0;
    }

    public int getKpca() {
        if (this.kpca == true){
            return 1;
        }
        return 0;
    }

    public String getKpcaKernelFunction() {
        return kpcaKernelFunction.toLowerCase();
    }
    
    
     
}
