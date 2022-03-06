def updateSupportedBtagDiscr(supportedBtagInfos, supportedBtagDiscr, supportedMetaDiscr):
    
    ## Update taggers in DeepHWWV1
    from PhysicsTools.NanoTuples.hwwTagger.pfMassDecorrelatedDeepHWWV1_cff import _pfMassDecorrelatedDeepHWWV1JetTagsProbs, _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs
    # update supportedBtagDiscr
    supportedBtagInfos.extend(["pfMassDecorrelatedDeepHWWV1TagInfos"])
    for disc in _pfMassDecorrelatedDeepHWWV1JetTagsProbs + _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs:
        supportedBtagDiscr[disc] = [["pfMassDecorrelatedDeepHWWV1TagInfos"]]
    # update supportedMetaDiscr
    for disc in _pfMassDecorrelatedDeepHWWV1JetTagsMetaDiscrs:
        supportedMetaDiscr[disc] = _pfMassDecorrelatedDeepHWWV1JetTagsProbs

    return supportedBtagInfos, supportedBtagDiscr, supportedMetaDiscr

## Import TagInfos additional to RecoBTag_cff
from PhysicsTools.NanoTuples.hwwTagger.pfMassDecorrelatedDeepHWWV1_cff import *