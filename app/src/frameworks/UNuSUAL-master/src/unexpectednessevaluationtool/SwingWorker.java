/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unexpectednessevaluationtool;

import java.awt.Desktop;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author labpi
 */
public class SwingWorker extends javax.swing.SwingWorker<Integer, String> {
    
    public UnexpectednessEvaluationFrame frame;
    public ParametersEvaluation parameters;
    
    public SwingWorker(UnexpectednessEvaluationFrame f, ParametersEvaluation p){
        frame = f;
        parameters = p;
    }

    @Override
    protected Integer doInBackground() throws Exception {
        
        frame.enableComponents(false);
        
        Runtime rt = Runtime.getRuntime();
        String[] commands = {"bash","evaluateUnexpectedness.sh"};
        Process proc = rt.exec(commands);
        InputStream stdout = proc.getInputStream();
        
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        String line;
        while((line = reader.readLine())!=null){
            frame.setBashCallOutput("Status: "+line);
        }
        
        try {
            if (parameters.getListRecommendationLists().keySet().size()==1){
                Desktop.getDesktop().open(new File(parameters.getOutputFolder()+"/"+parameters.getRecommendationListName((String) parameters.getListRecommendationLists().keySet().toArray()[0])));
            } else {
                Desktop.getDesktop().open(new File(parameters.getOutputFolder()));
            }
        
        } catch (IOException ex) {
            Logger.getLogger(UnexpectednessEvaluationFrame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        frame.enableComponents(true);
        return 1;
    }
    
}
