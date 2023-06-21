var chunk=function(arr,size){
    
    const no_of_splits=Math.ceil(length(arr)/size);
    var ans=new Array(no_of_splits);

    for (let i = 0; i < no_of_splits; i++) {
        ans[i]=new Array(size);
        for (let j=0;j<size;j++){
            var index=i*size+j;
            ans[i][j]=arr[index];
        }
        
    }
};