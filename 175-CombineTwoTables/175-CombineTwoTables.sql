-- Last updated: 7/16/2025, 8:14:53 PM
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state from person p left join address a 
on p.personid = a.personid
