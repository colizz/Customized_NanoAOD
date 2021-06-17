# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test_nanoTuples_mc2018 -n 10 --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v15_L1v1 --step NANO --nThreads 1 --era Run2_2018,run2_nanoAOD_106Xv1 --customise PhysicsTools/NanoTuples/nanoTuples_cff.nanoTuples_customizeMC --filein /store/mc/RunIISummer19UL18MiniAOD/GluGluToBulkGravitonToHHTo4B_M-1000_narrow_WZHtag_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/20000/86AAB896-106A-4D4E-9657-DDB87FAFD1EE.root --fileout file:nano_mc2018.root --customise_commands process.options.wantSummary = cms.untracked.bool(True)
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1

process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
# this should be tweaked by Crab3 Wraper
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('/store/mc/RunIISummer19UL18MiniAOD/GluGluToBulkGravitonToHHTo4B_M-1000_narrow_WZHtag_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/20000/86AAB896-106A-4D4E-9657-DDB87FAFD1EE.root'),
    fileNames = cms.untracked.vstring('file:/eos/user/q/qiguo/B2G/1lep/Test_File/2EF33A75-12EE-E242-B708-3709C312FE3D.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('mc2018 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)


# define filter
# finalJetsAK8 is used in for the NanoAOD fatJettable

process.FatJetsFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("finalJetsAK8"),
    minNumber = cms.uint32(1),
    )   

process.JetsAK8Count = cms.EDFilter("PATJetRefSelector",
    src = cms.InputTag("slimmedJetsAK8"),
    cut = cms.string("pt > 170")
    )

process.MuonCount = cms.EDFilter("PATMuonRefSelector",
    src = cms.InputTag("linkedObjects","muons"),
    cut = cms.string("pt > 50")
    )

process.ElectronCount = cms.EDFilter("PATElectronRefSelector",
    src = cms.InputTag("linkedObjects","electrons"),
    cut = cms.string("pt > 50")
    )

process.lepton = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag( "ElectronCount","MuonCount" ),
    cut = cms.string("pt > 50")
    ) 

process.leptonFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("lepton"),
    # src = cms.InputTag("ElectronCount"),
    minNumber = cms.uint32(1),
    )


# process.p1 = cms.Path ( process.JetsAK8Count * process.FatJetsFilter * process.MuonCount * process.ElectronCount* process.lepton * process.leptonFilter )
process.p1 = cms.Path ( process.MuonCount * process.ElectronCount* process.lepton * process.leptonFilter  )



# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:mc2018.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands,
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p1')
    ),
)




# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v15_L1v1', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
# process.schedule = cms.Schedule( process.nanoAOD_step, process.endjob_step, process.NANOAODSIMoutput_step)
process.schedule = cms.Schedule( process.nanoAOD_step, process.p1, process.endjob_step, process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from PhysicsTools.NanoTuples.nanoTuples_cff
from PhysicsTools.NanoTuples.nanoTuples_cff import nanoTuples_customizeMC 

#call to customisation function nanoTuples_customizeMC imported from PhysicsTools.NanoTuples.nanoTuples_cff
process = nanoTuples_customizeMC(process)

# End of customisation functions

# Customisation from command line


# process.options.wantSummary = cms.untracked.bool(True)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
