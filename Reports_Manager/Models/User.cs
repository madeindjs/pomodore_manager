using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Configuration;
using System.Data;
using System.Data.Entity;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class User
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public string Email { get; set; }
        public string Firstname { get; set; }
        public string Lastname { get; set; }
        [Required]
        public string Password { get; set; }
        

        public Boolean save()
        {
            SqlConnection sqlConnection = new SqlConnection("Data Source=AH734716\\SQLEXPRESS;Initial Catalog=Reports_Manager.Models.CarrierDataEntities;Integrated Security=True");

            try
            {
                sqlConnection.Open();

                string sqlCommand_str = String.Format(
                    "INSERT INTO [Users] ([Users].Email, [Users].Firstname, [Users].Lastname , [Users].Password) VALUES ('{0}' , '{1}', '{2}', '{3}')", 
                    Email, Firstname , Lastname , Password);

                SqlCommand sqlCommand = new SqlCommand(sqlCommand_str , sqlConnection);

                sqlCommand.ExecuteNonQuery();
                
            }
            catch(Exception e)
            {
                System.Diagnostics.Debug.WriteLine( e.Message );
                return false;
            }
            finally
            {
                sqlConnection.Close();
            }
            return true;

        }

    }
}