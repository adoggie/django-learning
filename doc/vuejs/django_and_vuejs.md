
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
