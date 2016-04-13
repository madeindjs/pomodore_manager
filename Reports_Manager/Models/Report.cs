using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class Report
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public int User_id { get; set; }
        [Required]
        public string Shop_id { get; set; }
        public string Serie { get; set; }
        public int Categoriy_id { get; set; }
        public DateTime Created_at { get; set; }
        public DateTime Updated_at { get; set; }
        public string Asked_by { get; set; }
        public string Notes { get; set; }
        public TimeSpan T_spend { get; set; }
        public TimeSpan T_travel { get; set; }
        public TimeSpan T_plus { get; set; }
        public string Description { get; set; }
        public string Analysis { get; set; }
        public string Facts { get; set; }
        public string Forecast { get; set; }

        public Boolean save()
        {
            SqlConnection sqlConnection = new SqlConnection("Data Source=AH734716\\SQLEXPRESS;Initial Catalog=Reports_Manager.Models.CarrierDataEntities;Integrated Security=True");

            try
            {
                sqlConnection.Open();

                string sqlCommand_str = String.Format(
                    "INSERT INTO [Reports] ([Reports].User_id, [Reports].Serie, [Reports].Shop_id ) VALUES ('{0}' , '{1}', '{2}')",
                    User_id, Serie, Shop_id);

                SqlCommand sqlCommand = new SqlCommand(sqlCommand_str, sqlConnection);

                sqlCommand.ExecuteNonQuery();

            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e.Message);
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