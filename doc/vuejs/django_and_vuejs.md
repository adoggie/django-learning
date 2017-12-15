
集成django和vuejs必须修改vue的修饰符 {{}} ,这里改为 [[ ]]

```html
<div id="block">
        [[ message ]]
        <select id="arr" v-model="selected">
            <option v-for="op in options" v-bind:value="op.value">[[op.text]]</option>
        </select>
        <span>selected: [[ selected ]]</span>
    </div>
    <script type="text/javascript">
        var vm = new Vue({
            delimiters: ['[[', ']]'],
            el: '#block',
            data: {
                selected: 2,
                options: [{text: 'apple', value: 1},
                    {text: 'pear', value: 2},
                    {text: 'grape', value: 3}
                ],
                message: 'this is warning message.'
            },
        })
    </script>

```


vuejs 实现对组件进行封装，包括内部属性和控制方法，数据的呈现方式。 
```html
    <div id="block">
        [[ message ]]
        <button id="btn" class="btn btn-danger btn-sm" v-on:click="show()">Message</button>
        <select id="arr" v-model="selected">
            <option v-for="op in options" v-bind:value="op.value">[[op.text]]</option>
        </select>
        <span>selected: [[ selected ]]</span>
    </div>

    var vm = new Vue({
        delimiters: ['[[', ']]'],
        el: '#block',
        data: {
            selected: 2,
            options: [{text: 'apple', value: 1},
                {text: 'pear', value: 2},
                {text: 'grape', value: 3}
            ],
            message: 'this is warning message.'

        },
        methods:{
            show:function () {
                this.selected+=1;
                if(this.selected > 3){
                    this.selected = 1;
                }
            }
        }

    });
```
