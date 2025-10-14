from iclabel_dataset.icldata import ICLabelDataset

icl=ICLabelDataset()
icl.download_trainset_features()
icldata = icl.load_semi_supervised()
