
#### _1_ 预处理
运行如下程序:

```
python preprocess_generate_training_dataset.py \
--dataset_root_dir dataset \
--dataset_folder_name datasetdemo
```



#### _2_ 训练网络
运行如下程序:

```
python train_hed.py --dataset_root_dir dataset \
                    --csv_path dataset/datasetdemo.csv \
                    --display_step 5
```


#### _3_ 测试
运行如下程序，处理一张图片:

```
python evaluate_hed.py --checkpoint_dir checkpoint \
                       --image test_image/test27.jpg \
                       --output_dir test_image
```




