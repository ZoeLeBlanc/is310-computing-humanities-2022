---
title: "Shared Resources and Annotations"
permalink: /shared-resources-and-annotations/
# toc: true
# toc_sticky: true
author_profile: false
datatable: true
layout: single
classes: wide
---

<!-- {% include test-table.html %} -->

<!-- <div class="datatable-begin"></div>

{% include_relative relevant-materials-table.md %}

<div class="datatable-end"></div> -->

### Hypothesis Annotations

<!-- <div class="datatable-begin"></div>

{% include_relative hypothesis-table.md %}

<div class="datatable-end"></div> -->

<!-- <input id='myInput' onkeyup='searchTable()' type='text'> -->

<!-- <table id='myTable'>
   <tr>
      <td>Apple</td>
      <td>Green</td>
   </tr>
   <tr>
      <td>Grapes</td>
      <td>Green</td>
   </tr>
   <tr>
      <td>Orange</td>
      <td>Orange</td>
   </tr>
</table> -->



<!-- <table id="relevant-materials-table">
  {% for row in site.data.relevant_materials %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}
    <tr>
      {% for pair in row %}
        <td>{{ pair[1] }}</td>
      {% endfor %}
    </tr>
    <!-- {% tablerow pair in row %}
      <td>{{ pair[1] }}</td>
    {% endtablerow %}
  {% endfor %}
</table>

<script>
function searchTable() {
    var input, filter, found, table, tr, td, i, j;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        for (j = 0; j < td.length; j++) {
            if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                found = true;
            }
        }
        if (found) {
            tr[i].style.display = "";
            found = false;
        } else {
            tr[i].style.display = "none";
        }
    }
}
</script> -->

<!-- Include the standard DataTables bits -->
<!-- <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.12.0/css/jquery.dataTables.css"> -->
<!-- <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script> -->
<!-- <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.12.0/js/jquery.dataTables.js"></script> -->

<!-- <script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.12.1/b-2.2.3/cr-1.5.6/date-1.1.2/fc-4.1.0/fh-3.2.3/r-2.3.0/sc-2.0.6/sb-1.3.3/sp-2.0.1/datatables.min.js"></script> -->
<!-- <script type="text/javascript" src="https://cdn.datatables.net/v/bm/dt-1.12.1/b-2.2.3/cr-1.5.6/date-1.1.2/fc-4.1.0/fh-3.2.3/r-2.3.0/sc-2.0.6/sb-1.3.3/sp-2.0.1/datatables.min.js"></script> -->

<!-- First, this walks through the tables that occur between ...-begin
and ...-end and add the "datatable" class to them.
Then it invokes DataTable's standard initializer
Credit here: http://www.beardedhacker.com/blog/2015/08/28/add-class-attribute-to-markdown-table/
-->

<!-- <script>
    $(document).ready(function () {
        $.noConflict();
        $('div.datatable-begin').nextUntil('div.datatable-end', 'table').addClass('display');
        $('table.display').DataTable({
            paging: true,
            stateSave: true,
            searching: true
        });
    });
</script> -->
