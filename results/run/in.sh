#!/usr/bin/env bash

cd "/workspaces/LadybugTools/results/run"
"/EnergyPlus-25.1.0-68a4a7c774-Linux-Ubuntu22.04-x86_64/energyplus" -w "/workspaces/LadybugTools/CAN_QC_Montreal-McTavish.716120_CWEC2016/CAN_QC_Montreal-McTavish.716120_CWEC2016.epw" -i "/EnergyPlus-25.1.0-68a4a7c774-Linux-Ubuntu22.04-x86_64/Energy+.idd" -x