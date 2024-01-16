https://stackoverflow.com/questions/25088699/make-fish-functions-private

```
function outer
    function inner_func
        echo "I still find this function via automplete."
        echo "Not anymore!!"
        functions -e inner_func
    end
    # Let's test this!
    inner_func
end


$ outer
I still find this function via automplete.
Not anymore!!
$ inner_func
fish: Unknown command 'inner_func'
```

