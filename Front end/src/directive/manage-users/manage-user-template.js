<>
<h1>{{title}}</h1>
<h4><button ng-click="refreshUsers()">Refresh</button></h4>
<h4><button ng-click="connectPython()">Connect Python</button></h4>
<table>
<th>id</th>
<th>name</th>
<th>birthday</th>
<th>age</th>
<th>sex</th>
<th>address</th>
<tbody ng-repeat="user in listUsers">
  <tr>
    <td>{{user.id}}</td>
    <td>{{user.name}}</td>
    <td>{{user.birthday | date: "dd/MM/yyyy"}}</td>
    <td>{{user.age}}</td>
    <td>{{user.sex}}</td>
    <td>{{user.address}}</td>
  </tr>
</tbody>
</table>
</>