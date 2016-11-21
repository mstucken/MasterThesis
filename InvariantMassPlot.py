print "Starting"

import ROOT as rt
import numpy as np

f=rt.TFile("DisplacedTop_Run2_TopTree_Study_DYJetsToLL_M-50toInf_Madgraph_MuMu_NoBlinding_1.root","read")
f.ls()

#t = f.Get("tree")
#b=t.GetBranch("invMass_mumu")

ch = rt.TChain("tree","tree")
ch.Add("DisplacedTop_Run2_TopTree_Study_DYJetsToLL_M-50toInf_Madgraph_MuMu_NoBlinding_1.root")


lvmu1=rt.TLorentzVector()
lvmu2=rt.TLorentzVector()
lv2= 0

hist = rt.TH1F("Invariance Mass", " ", 20, 20, 200)

histpT = rt.TH1F("muon pT"," ",100,0,500);
histeta = rt.TH1F("muon eta"," ",100,-3.14,3.14);
histphi = rt.TH1F("muon phi"," ",100,-3.14,3.14);
histd0 = rt.TH1F("muon d0"," ",100,0,0.05);

for iev in ch:
	if iev.nMuons != 2:
		continue
	lvmu1.SetPtEtaPhiE(iev.pt_muon[0],iev.eta_muon[0],iev.phi_muon[0],iev.E_muon[0])
	lvmu2.SetPtEtaPhiE(iev.pt_muon[1],iev.eta_muon[1],iev.phi_muon[1],iev.E_muon[1])
	lv2 = (lvmu1 + lvmu2).M()
	hist.Fill(lv2)
	for imu in range(0,iev.nMuons):
		histpT.Fill(iev.pt_muon[imu])
		histeta.Fill(iev.eta_muon[imu])
		histphi.Fill(iev.phi_muon[imu])
		histd0.Fill(iev.d0_muon[imu])
    

# Drawing the histograms 
# The invariant mass plot is made seperatly
# The pT, eta, phi, d0 plots are plotted on the same canvas

t=rt.TLatex
c1 = rt.TCanvas(" "," ",900,700)
rt.gStyle.SetOptStat(0);
c1.Divide(2,2,0.02,0.002)

c1.cd(1);
rt.gPad.SetTickx(2)
rt.gPad.SetTicky(2)
rt.gPad.SetLogy()
histpT.GetYaxis().SetTitle("Entries")
histpT.GetXaxis().SetTitle("pT [Gev]")
histpT.GetYaxis().SetTitleOffset(1.6)
histpT.Draw();

c1.cd(2);
rt.gPad.SetTickx(2);
rt.gPad.SetTicky(2);
histeta.GetYaxis().SetLabelOffset(0.01)
histeta.GetYaxis().SetTitle("Entries")
histeta.GetXaxis().SetTitle("muon $\eta$")
histeta.GetYaxis().SetTitleOffset(1.6)
histeta.Draw();

c1.cd(3);
rt.gPad.SetTickx(2);
rt.gPad.SetTicky(2);
histphi.GetYaxis().SetTitle("Entries")
histphi.GetXaxis().SetTitle("muon $\phi$")
histphi.GetYaxis().SetTitleOffset(1.6)
histphi.SetAxisRange(0, 900,"Y");
histphi.Draw();

c1.cd(4);
rt.gPad.SetTickx(2);
rt.gPad.SetTicky(2);
histd0.GetYaxis().SetTitle("Entries")
histd0.GetXaxis().SetTitle("muon |d0| [cm]")
histd0.GetYaxis().SetTitleOffset(1.6)
histd0.Draw();

c2 = rt.TCanvas()
rt.gPad.SetTickx(2);
rt.gPad.SetTicky(2);
hist.GetYaxis().SetTitle("Entries")
hist.GetXaxis().SetTitle("M_{\mu\mu} [Gev]")
hist.GetYaxis().SetTitleOffset(1.6)
hist.Draw()

