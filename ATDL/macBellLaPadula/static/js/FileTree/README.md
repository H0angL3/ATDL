File tree
=========

File tree is a jQuery plugin that aims to make implementation of file tree stuctures easy. File tree provides fixed, sortable and selectable file tree's with Twitter Bootstrap (3) flavour.

Demo
----
[Check out File tree in action!][1]

Getting started
---------------

Create a div with an id inside your html file.
```html
<div id="filetree"></div>
```

Include CSS (Bootstrap & file-tree)
```html
<link href="path_to_bootstrap/bootstrap.min.css" rel="stylesheet">
<link href="path_to_file-tree/file-tree.min.css" rel="stylesheet">
```

Include JS (jQuery, jQuery UI, Bootstrap, nestedSortable & file-tree.min.js)
```html
<script src="path_to_jquery/jquery.min.js"></script>
<script src="path_to_jquery_ui/jquery-ui.js"></script>
<script src="path_to_bootstrap/bootstrap.min.js"></script>
<script src="path_to_nestedSortable/jquery.mjs.nestedSortable.js"></script>
<script src="path_to_file-tree/file-tree.min.js"></script>
```

Initialize File tree!
```html
<script type="text/javascript">
    $(function () {
        // Replace data with your own json data
        var data = [{
           id: 'dir-1',
            name: 'Root',
            type: 'dir',
            children: [
                {
                    id: 'file-1',
                    name: 'File tree',
                    type: 'zip',
                    url: 'https://github.com/MathiasD90/file-tree/archive/master.zip'
                }
            ]
       }];

        $('#filetree').treebuilder({ data: data });
    });
</script>
```

Options
-------
**Sortable tree**
```javascript
  $('#filetree').treebuilder({
      data: data,
      sortable: true
  });
```

**Selectable tree**
```javascript
  $('#filetree').treebuilder({
      data: data,
      selectable: true
  });
```

Functions
---------
**toObject**
```javascript
var tree = $('#filetree').treebuilder({data: data});
tree.fileTree('toObject')
```

**toJson**
```javascript
var tree = $('#filetree').treebuilder({data: data});
tree.fileTree('toJson')
```
Events
------
**itemSelected**
Only works when the option: `selectable = true`
```javascript
var tree = $('#filetree').treebuilder({data: data});
tree.bind('itemSelected', function(e, el){
    var id = $(el).data('id');
    var name = $(el).data('name');
    var type = $(el).data('type');
});
```

  [1]: http://mathiasd90.github.io/file-tree/demo/index.html